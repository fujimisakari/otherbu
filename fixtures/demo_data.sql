# ユーザー
UPDATE `oauth_user` SET page_id = 0 WHERE id = 6;

# ブックマーク
DELETE FROM `setting_bookmark` WHERE user_id = 6;
INSERT INTO `setting_bookmark` VALUES
(174,6,'',46,'YouTube - Broadcast Yourself','http://youtube.co.jp',1,1,'2015-05-07 00:00:00'),
(175,6,'',46,'ニコニコ動画(原宿)','http://www.nicovideo.jp/video_top/',2,1,'2015-05-07 00:00:00'),
(176,6,'',47,'Facebook - フェイスブック - ログイン (日本語)','http://facebook.com',1,1,'2015-05-07 00:00:00'),
(177,6,'',47,'Twitter','https://twitter.com/',2,1,'2015-05-07 00:00:00'),
(178,6,'',47,'ソーシャル・ネットワーキング サービス [mixi(ミクシィ)]','http://mixi.jp/',3,1,'2015-05-07 00:00:00'),
(179,6,'',48,'Google','http://google.co.jp',1,1,'2015-05-07 00:00:00'),
(180,6,'',48,'Yahoo! JAPAN','http://yahoo.co.jp',2,1,'2015-05-07 00:00:00'),
(181,6,'',49,'カミソリ・髭剃りとメンズグルーミングの専門店　｜　カミソリ倶楽部','http://www.kamisoriclub.co.jp/',3,1,'2015-05-07 00:00:00'),
(182,6,'',49,'日本大相撲協会公式サイト','http://www.sumo.or.jp/',2,1,'2015-05-07 00:00:00'),
(183,6,'',49,'グルメ・レストランガイド [食べログ]','http://tabelog.com/',1,1,'2015-05-07 00:00:00');

# カテゴリ
DELETE FROM `setting_category` WHERE user_id = 6;
INSERT INTO `setting_category` VALUES
(46,6,'','動画サイト',2,2,3,1,1,'2015-05-07 00:00:00'),
(47,6,'','SNS',3,1,4,1,1,'2015-05-07 00:00:00'),
(48,6,'','ポータルサイト',1,1,9,0,1,'2015-05-07 00:00:00'),
(49,6,'','お気に入り',1,2,16,1,1,'2015-05-07 00:00:00');

# デザイン
DELETE FROM `setting_design` WHERE user_id = 6;
INSERT INTO `setting_design` VALUES (6,6,0,'#444444','#ffd39b',1,'#ffffff','no-repeat','jpg',1,'2015-05-07 00:00:00');

# ページ
DELETE FROM `setting_page` WHERE user_id = 6;
