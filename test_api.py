import requests

if __name__ == "__main__":
    # files = {'file': ("test.mp4", open(r'/mnt/2t/home/datasets/TB/test.mp4', 'rb'))}
    files = {'file': ("test_lintao2.mp4", open(r'/mnt/2t/home/zhengbowen/person_search_demo-master/data/samples/test_lintao2.mp4', 'rb'))}
    # response = requests.post("http://172.16.6.141:30080/action/", data=None, files=files, verify=False, stream=True)
    # response = requests.post("http://172.16.6.141:30080/reid/", data=None, files=files, verify=False, stream=True)
    response = requests.post("http://127.0.0.1:5000/reid/", data=None, files=files, verify=False, stream=True)
    # datas = {'video_path': "./test_video", 'label_txt': "./label.txt"}
    # response = requests.post("http://172.16.6.141:30080/reid/pr", json=datas)
    print(response.status_code)
    print(response.text)
