from typing import Union
import requests
from .api_typing import PostsBrief, SearchResult


class SchdocApi:
    wp_root: str
    _categories_map: dict[int, str]

    def __init__(self, wp_root: str):
        '''
        wp_root — The URL of the root of the WordPress instance.
        '''
        self.wp_root = wp_root
        self._categories_map = dict()

    def _build_uri(self, method: str):
        return f"{self.wp_root}/wp-json/wp/v2/{method}"

    def _get_json(self, url: str, params: dict[str, str]):

        r = requests.get(url, params)  # type: ignore

        if r.status_code != 200:
            raise Exception(r.text)

        return r.json()  # type: ignore

    def get_category_name_map(self, cid: Union[int, str]) -> str:
        return self.get_category_name(int(cid))

    def get_category_name(self, cid: int, force_new: bool = False) -> str:
        '''
        Get the category name of <cid>.

        force_new — Force fetching the <cid> from the API instead of getting from our cache.
        '''
        cname = ''

        if cid in self._categories_map and not force_new:
            cname = self._categories_map[cid]
        else:
            cname = self._get_json(
                self._build_uri(f'categories/{cid}'),
                {'_fields': 'name'}
            )['name']
            self._categories_map[cid] = cname

        return cname

    def get_posts_brief(self, page: int = 1, category: str = '') -> list[PostsBrief]:
        '''
        Get the brief information of the posts in the CMS.

        page — The page to be fetched in the CMS API.
        query — What to search?
        category — What is the only categories, separated in ',', to fetch?
        '''
        posts = self._get_json(
            self._build_uri('posts'),
            {'page': str(page), 'categories': category,
             '_fields': 'id,title,categories'}
        )

        return posts

    def search(self, search: str, page: int = 1) -> list[SearchResult]:
        return self._get_json(
            self._build_uri('search'),
            {'page': str(page), 'search': search,
                '_fields': 'id,title'}
        )

    def get_post_content(self, post_id: int) -> str:
        post = self._get_json(
            self._build_uri(f'posts/{post_id}'),
            {'_fields': 'content'}
        )['content']['rendered']

        return post

    def batch_convert_categories_in_PostsBrief(self, pb: list[PostsBrief]) -> list[PostsBrief]:
        '''
        Batch converting the number categories in <pb> to the human-readable categories.
        '''
        for i in pb:
            i['categories'] = list(
                map(self.get_category_name_map, i['categories']))
        return pb
