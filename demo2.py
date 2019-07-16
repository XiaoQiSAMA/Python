# import  requests
# #
# # headers = {
# #     'Origin': 'https://www.bilibili.com',
# #     'Host': 'www.bilibili.com',
# #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
# #     'Referer': 'https://www.bilibili.com/video/av11878734/',
# #     'Cookie': "_uuid=A15D6555-155C-6C51-4C75-9301DBBA62DE72428infoc; buvid3=8AEAED62-DC00-42B2-A6AE-F92B99F1993E47189infoc; LIVE_BUVID=AUTO7815521154719994; sid=7jy9ws1l; stardustvideo=1; CURRENT_FNVAL=16; im_notify_type_24219561=0; fts=1552637992; UM_distinctid=16984dde73d3c3-0d626c82d86dac-7a1b34-149c48-16984dde73e170; pgv_pvi=3882159104; CNZZDATA2724999=cnzz_eid%3D1586699943-1553847979-https%253A%252F%252Fwww.bilibili.com%252F%26ntime%3D1554273759; gr_user_id=3fe2834c-b177-4acf-9530-91a86efa6b53; grwng_uid=ddb19c20-317e-43fa-83b6-08519852c564; rpdid=|(J~l~|lR||)0J'ullY|uRklY; finger=b3372c5f; stardustpgcv=0; balh_server_inner=https://www.biliplus.com; balh_=cos; balh_upos_server=cos; im_seqno_24219561=9483; im_local_unread_24219561=0; bp_t_offset_24219561=276014973768925320; CURRENT_QUALITY=32",
# #     'Host': "www.bilibili.com"
# # }
# # r = requests.get('https://www.bilibili.com/video/av11878734/', headers=headers)
# # print(r.status_code)
# # with open('demo1.html', 'wb') as f:
# #     f.write(r.content)

a = [1, 2, 3, 4, 5]
for i in range(10, 0, -1):
    print(i)
a.insert(2, 'q')
# print(a)