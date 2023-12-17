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
