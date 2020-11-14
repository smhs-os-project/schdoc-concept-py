from typing import TypedDict, Union


class PostsBrief_Title(TypedDict):
    '''
    The contained type of PostsBrief.title
    '''
    rendered: str


class PostsBrief(TypedDict):
    '''
    The return type of get_posts_brief.
    '''

    id: int
    title: PostsBrief_Title
    categories: Union[list[str], list[int]]


class SearchResult(TypedDict):
    '''
    The return type of search.
    '''

    id: int
    title: str
