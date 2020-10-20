class Translation(object):
    START_TEXT = """嗨,
这是一个电报HTTP直连上传机器人！

<b>请发送一个下载直连给我，我会帮您下载并以文件或视频格式上传到电报</b>

/help 更多详细内容..

加入里番频道 : @banbilibili
加入讨论群组 : @animeforh
© @lfurluploadbot"""
    RENAME_403_ERR = "对不起，你没有权限去重命名文件"
    ABS_TEXT = " 欢迎使用本机器人"
    UPGRADE_TEXT = "<b>👉 加入里番频道 @banbilibili </b>  /help 获取更多内容"
    FORMAT_SELECTION = "选择你想要的格式: <a href='{}'>文件大小为估计值</a> \n如果你想要设置自定义缩略图, 请先发送图片或者在按下下方按钮后快速发送图片.\n你可以使用 /deletethumbnail 来删除系统自动生成的文件"
    SET_CUSTOM_USERNAME_PASSWORD = """如果你想下载会员视频请按以下格式:
URL | filename | username | password"""
    NOYES_URL = "@robot URL detected. "
    DOWNLOAD_START = "正在下载中"
    UPLOAD_START = "正在上传中"
    RCHD_BOT_API_LIMIT = "文件大小超过最大限制 (50MB). 无需担心，正在上传."
    RCHD_TG_API_LIMIT = "下载耗时 {} 秒.\n当前文件大小: {}\n对不起，由于TG官方API限制，我无法上传超过1.5GB以上大小的文件"
    AFTER_SUCCESSFUL_UPLOAD_MSG = "如果觉得我有用的话请加入频道进行讨论 : @animeforh"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \n加入 : @banbilibili \nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "请 /upgrade 您的订阅."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. 免费用户上传限制: {}\n请 /upgrade 您的订阅.\n如果您认为这是一个BUG请联系 <a href='https://telegram.dog/suka25'>@suka25</a>"
    SAVED_CUSTOM_THUMB_NAIL = "自定义 视频 / 文件 缩略图已保存. 该图将会用于这个 视频 / 文件."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ 自定义图片清楚成功."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ 媒体文件清楚成功"
    SAVED_RECVD_DOC_FILE = "文档下载成功"
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "未发现自定义缩略图"
    NO_VOID_FORMAT_FOUND = "错误...\n<b>YouTubeDL</b> 报告: {}"
    USER_ADDED_TO_DB = "用户 <a href='tg://user?id={}'>{}</a> 添加至 {} 到 {}."
    CURENT_PLAN_DETAILS = """当前套餐详情
--------
Telegram ID: <code>{}</code>
Plan name: 免费用户
Expires on: 31/12/2020"""
    HELP_USER = """嗨，我是文件上传机器人..
    
1. 发送下载直连 (URL|名称及后缀).
2. 发送自定义缩略图 (可选).
3. 选择按钮.
   SVideo - 以视频文件发送，带截图
   DFile  - 以文件形式发送，带截图
   Video  - 以视频形式发送，不带截图
   DFile  - 以文件形式发送，不带截图
   
<b>👉 加入我们的频道 :</b> 👉 <a href="https://t.me/banbilibili"> @banbilibili</a>

--------
发送 /me 获取当前套餐

加入老司机频道 : @banbilibili
© @animeforh"""
    REPLY_TO_DOC_GET_LINK = "回复一个TG视频或文件获取高速下载链接"
    REPLY_TO_DOC_FOR_C2V = "回复一个视频文件进行转码"
    REPLY_TO_DOC_FOR_SCSS = "回复一个TG视频文件获取截图"
    REPLY_TO_DOC_FOR_RENAME_FILE = "回复一个视频文件 /rename 进行重命名（支持自定义缩略图）"
    AFTER_GET_DL_LINK = "直链 <a href='{}'>已生成</a> 有效期 {} 天.\n© @lfurluploadbot"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """格式: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "首次发送 /downloadmedia 至任何媒体文件，则它将会自动下载到本地. \n发送 /storageinfo 了解文件当前存储信息."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "视频时长: {}\n发送 /clearffmpegmedia 删除本地视频.\n发送 /trim HH:MM:SS [HH:MM:SS] 去截取一张图片 / 小段视频, 从上方视频."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "文件已存在. 请发送 /storageinfo 了解文件当前存储位置"
    USER_DELETED_FROM_DB = "用户 <a href='tg://user?id={}'>{}</a> 已从数据库中删除."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "回复一个媒体文件 (MKV), 提取嵌入流"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "回复 /generatecustomthumbnail 至一个媒体相册, 生成自定义缩略图"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "媒体相册只包含两张图片.请重新上传媒体相册再进行尝试, 或者只上传两张图片至一个媒体相册"
    INVALID_UPLOAD_BOT_URL_FORMAT = "链接格式不正确. 请确保链接为 http:// 或 https://. 您可以设置自定义文件名，格式： URL | 文件名.后缀"
    ABUSIVE_USERS = "你没有使用权限，如果你认为有错误, 请检查 /me 移除限制."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.dog/FFMpegRoBot"
    EXTRACT_ZIP_INTRO_ONE = "先发送一个压缩文件, 然后回复 /unzip 解压该文件."
    EXTRACT_ZIP_INTRO_THREE = "分析已接收文件. ⚠️ 这会花费一些时间. 请耐心等候. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "对不起，解压文件时出现错误. 请检查步骤是否正确, 如果这是个问题, 请提交给 <a href='https://telegram.dog/suka25'>@suka25</a>"
    EXTRACT_ZIP_STEP_TWO = """选择文件名及使用一下设置上传.
你可以使用 /rename 命令在接受文件时更改文件名及缩略图"""
    CANCEL_STR = "进程取消"
    ZIP_UPLOADED_STR = "上传 {} 个文件 在 {} 秒内"
    FREE_USER_LIMIT_Q_SZE = """无法运行.
免费用户限制为每30分钟一个请求
/upgrade 或等待30分钟"""
    SLOW_URL_DECED = "这似乎是一个非常慢的链接. 不妨试试使用代理."
