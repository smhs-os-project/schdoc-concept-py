'''
The Concept of Schdoc.
'''
from SchdocLib.api_typing import PostsBrief, SearchResult
from SchdocLib.SchdocApi import SchdocApi
from os import environ as env


def visualize_posts_brief(pb: PostsBrief) -> str:
    return f"  {pb['id']}) {pb['title']['rendered']}"


def visualize_search_result(sr: SearchResult) -> str:
    return f"  {sr['id']}) {sr['title']}"


def ui_search() -> str:
    return input("您要搜尋什麼：")


def ui_main() -> str:
    print('- Schdoc: Concept -')
    print()
    print('  sa)  顯示所有知識庫文章')
    print('  se)  搜尋知識庫文章')
    print('  sh)  查看文章全文')
    print('  ex)  結束 Schdoc: Concept')
    print()
    return input("請選擇: ")


def log_search(api: SchdocApi) -> None:
    s = ui_search()
    sr = api.search(s)

    for i in sr:
        print(visualize_search_result(i))


def log_showall(api: SchdocApi) -> None:
    pb = api.get_posts_brief()

    for i in map(visualize_posts_brief,
                 api.batch_convert_categories_in_PostsBrief(pb)):
        print(i)


def log_showfull(api: SchdocApi) -> None:
    aid = input("你要查看哪篇文章(數字): ")
    print(api.get_post_content(int(aid)))


def main():
    api: SchdocApi
    try:
        api = SchdocApi(env['SCHDOC_SITE_URL'])
    except (KeyError):
        print("請先指定 'SCHDOC_SITE_URL' 環境變數。")
        print("可指向任何一個支援 WP RESTful API 的 WP 站台。")
        exit(1)

    user_choice = ui_main()

    if user_choice == 'sa':
        log_showall(api)
    elif user_choice == 'se':
        log_search(api)
    elif user_choice == 'sh':
        log_showfull(api)
    elif user_choice == 'ex':
        exit(0)
    else:
        main()

    return


main()
