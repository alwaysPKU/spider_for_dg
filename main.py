import get_mingxing_dict as get_mingxing


if __name__ == '__main__':
    minging_url_dic = get_mingxing.get_mingxingurl_dict('./source_data/20180117.txt')
    print(minging_url_dic)
    print(len(minging_url_dic))
