# UEECnotes

## 一些指令

### 生成requirement.txt

'''bash
pip freeze > requirements.txt
'''

### 安装requirement.txt中的依赖项

'''bash
pip install -r requirements.txt
'''

### 收集静态文件（nginx部署用）

'''bash
python manage.py collectstatic
'''

### 未上传.env邮箱信息

## 下载项目后要干的事
### 让自己的编辑器装环境
pip install -r requirements.txt
### 迁移数据库（model -> sqlite3）
python manage.py makemigrations
python manage.py migrate
### 创建超级用户（superuser）用来登录....../admin
python manage.py create superuser
