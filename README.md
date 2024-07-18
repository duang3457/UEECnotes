# UEECnotes

## 该项目为UEEC同学提供支持
### 功能模块
1、UEEC计分内容笔记：包括作业要求，格式模板，算分点，教师标准，往年高分作业（仅供参考格式，抄袭后果很严重）等
2、澳留子萌新交流论坛：包括作业交流板块、交友组局板块、经验分享板块、求助帖等。

## 一些指令

### 生成requirement.txt（在新导入包后使用）

'''bash
pip freeze > requirements.txt
'''

### 未上传.env邮箱信息

## 下载项目后要干的事

### 建虚拟环境（下面用python3.3以上自带的venv模块建虚拟环境，也可以用其他方式）

python3 -m venv myenv(这个参数是环境名)

### 激活虚拟环境

.\myenv\Scripts\activate

### 装依赖/包（根据requirements.txt下载包）

pip install -r requirements.txt

### 迁移数据库（model -> mysql）

python manage.py makemigrations # 生成迁移文件
python manage.py migrate # 根据迁移文件更变数据库

### 在项目根目录下建一个.env文件（目前里面有发注册确认邮件的邮箱账号和密码），内容格式如下：

EMAIL_HOST_USER=XXXX@XXXX.com
EMAIL_HOST_PASSWORD=XXXXXXX
（填自己小号邮箱进行测试）

### 创建超级用户（superuser）用来管理后台（包括登录）....../admin

python manage.py create superuser
