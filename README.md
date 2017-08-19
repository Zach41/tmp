# 操作手册
### 1. 安装apktool
*Prerequisites*：Java 1.7 or later

1. 下载运行脚本[script](https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool)，存储为`apktool`
2. 下载apktool，从[apktools](https://bitbucket.org/iBotPeaches/apktool/downloads/)选择最新版本下载
3. 重命名下载的apktool为`apktool.jar`
4. 将运行脚本移到/usr/local/bin下或者是环境变量`PATH`指定的路径下
5. 修改`apktool`文件的权限：`chmod +x apktool`
5. 尝试在终端中输入`apktool --version`，如果正确输出，那么安装完毕

### 2. 安装sklearn
*Prerequisites*: Python 2.7 and pip installed

pip可能需要更换国内的源，更换到阿里云的镜像源修改`~/.pip/pip.conf`文件（如果不存在，就创建一个）
```
[global]
trusted-host =  mirrors.aliyun.com
index-url = http://mirrors.aliyun.com/pypi/simple
```

在cmd运行`pip install -U scikit-learn`即可

### 3. 运行代码

```shell
python run.py [OPSEQ_LEN] [ALGORITHM]
```
`ALGORITHM`可采用的值为
- SVM
- KNN
- DT (for decision tree)
例如指定长度为2， 算法采用决策树，那么运行
```
python run.py 2 DT
```

### 转换APK
如果要将APK文件转换成文本文件，执行以下命令：
```shell
python run_opcode_seq_create.py [apk_directory] [tmp_directory] [opseq_directory]
```
- apk_directory: 指定apk文件所在的目录
- tmp_directory: 一个临时目录(指定tmp即可)
- opseq_directory: 制定生成的字节码文本所在的目录

### 训练并测试
- 如果是恶意样本，将转换之后的样本放到`malwares_opseq`目录下的`training_set`目录中
- 如果是正常样本，将转换之后的样本放到`benign_opseq`目录下的`training_set`目录中

对于测试样本，测试样本放到`test_opseq`下即可，但是如果样本是：
- 恶意样本，文本命名规则为`malware_xxx`，即要用`malware`开头
- 正常样本，文本命名规则为`benign_xxx`，即以`benign`开头


