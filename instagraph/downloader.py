from instagraph.utils import get_response, prepare_urls
import re


class Dowloader():
    def __init__(self):
        pass

    def download(self, url: str):
        vid_url = prepare_urls(re.findall(
            '"video_url":"([^"]+)"', get_response(url=url)))
        pic_url = prepare_urls(re.findall(
            '"display_url":"([^"]+)"', get_response(url=url)))
        result = []
        if vid_url:
            result.append(vid_url)
        if pic_url:
            result.append(pic_url)
        if not (vid_url or pic_url):
            return None
        return result
