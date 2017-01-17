
TRUNCATE `oauth_user`;
INSERT INTO `oauth_user` VALUES (1,'facebook',100000000000000,'debug user','debug.user','AAACbJuimgFIBAMtwe15nPjyXImczsxtimgNgDjyK7URk1xnatfAmmMfISiimdgN5Yz0R2mqj5evwMuZAFUwLTJ9ls7nTWkwpwufagZDZD', '', 0, 0, 0, '2012-05-11 01:59:27', '2012-05-11 01:59:27');

TRUNCATE `oauth_passport`;
INSERT INTO `oauth_passport` VALUES (1,1,'6ad8bf8d-379f-40b0-815a-9bb2e5b54082','2012-05-11 01:59:27');

TRUNCATE `setting_bookmark`;
INSERT INTO `setting_bookmark` VALUES
(1,1,'',1,'YouTube - Broadcast Yourself','http://youtube.co.jp',1,1,'2012-05-11 01:59:27'),
(2,1,'',1,'ニコニコ動画(原宿)','http://www.nicovideo.jp/video_top/',2,1,'2012-05-11 01:59:27'),
(3,1,'',2,'Facebook - フェイスブック - ログイン (日本語)','http://facebook.com',1,1,'2012-05-11 01:59:27'),
(4,1,'',2, 'Twitter','https://twitter.com/',2,1,'2012-05-11 01:59:27'),
(5,1,'',2, 'ソーシャル・ネットワーキング サービス [mixi(ミクシィ)]','http://mixi.jp/',3,1,'2012-05-11 01:59:27'),
(6,1,'',3, 'Google','http://google.co.jp', 1,1,'2012-05-11 01:59:27'),
(7,1,'',3, 'Yahoo! JAPAN','http://yahoo.co.jp', 2,1,'2012-05-11 01:59:27'),
(8,1,'',4, 'カミソリ・髭剃りとメンズグルーミングの専門店　｜　カミソリ倶楽部','http://www.kamisoriclub.co.jp/',3,1,'2012-05-11 01:59:27'),
(9,1,'',4, '日本大相撲協会公式サイト','http://www.sumo.or.jp/',2,1,'2012-05-11 01:59:27'),
(10,1,'',4, 'グルメ・レストランガイド [食べログ]','http://tabelog.com/',1,1,'2012-05-11 01:59:27');

TRUNCATE `setting_category`;
INSERT INTO `setting_category` VALUES
(1,1,'','動画サイト',2,2,3,1,1,'2012-05-11 01:59:27'),
(2,1,'','SNS',3,1,4,1,1,'2012-05-11 01:59:27'),
(3,1,'','ポータルサイト',1,1,9,0,1,'2012-05-11 01:59:27'),
(4,1,'','お気に入り',1,2,16,1,1,'2012-05-11 01:59:27');

TRUNCATE `setting_design`;
INSERT INTO `setting_design` VALUES (1,1,0,'#444444','#ffd39b',1,'#ffffff','no-repeat','jpg',1,'2012-05-11 01:59:27');

TRUNCATE `setting_deletemanager`;
INSERT INTO `setting_deletemanager` VALUES (1,1,'','','');
