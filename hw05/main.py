import re
m = re.match(r'(..{20})(..{22})(..{20})(..{20})', 
            '我的电子邮件tom@gmail.com.  将什么发送到jerry123@163.com或者3123432@qq.com.     若遇特殊情况拨打18222061703   ' )
re.findall(r'[^\._-][\w\.-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+', m.group(1))
re.findall(r'[^\._-][\w\.-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+', m.group(2))
re.findall(r'[^\._-][\w\.-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+', m.group(3))
re.findall(r'^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}', m.group(4))
