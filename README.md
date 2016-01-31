# DT228B LAB SHEET 2
######Python Lab for college

In this lab you will be required to write a Python program for checking the integrity of a string or file. 
Your program must be able computing hash code for SHA-1, SHA-256, SHA-512 and SHA-3. 
You can use any Operating System such as Windows, Linux or Mac OS X. 
Make sure that you are program is documented. It is important that your program is uploaded in GitHub as well or any other web based repository service.

_______________________________________________________

My first attempt using Pyhton, i come from a .NET background favourite language C# 
Also im not familiar with using GIT HUB, I come from a Team Foundation Server background so a bit of a learning curve.

I choose Pycharm EDU Edition as my IDE.

I have used the following Operating Systems just to see what differs here with developing in Python

- Ubuntu 15,
- Windows 10,
- Mac OSX 

For the SHA3 Encoding task i used pysha3 0.3
Available here [https://pypi.python.org/pypi/pysha3/]

I installed it via an executable on windows and I also installed it via the terminal on the Linux based OS's
______________________________________________________________________________________


###### Installing library
Navigate to downloaded files in terminal

Run in terminal 

```python
sudo python setup.py install
```

Then add the pysha3 library as an external reference in PyCharm and its ready to use or you can copy the _sha3 folder into you project.
Located : pysha3-0.3\Modules

__________________________________________________________
###### Project Layout 
Project is a console application containing 1 class called MyEncryptor.py
This class contains the various methods required
Located in DT228B_PYTHON_LAB2/DT228B_LIB/MyEncryptor.py

The project also contains a sample text file called sample_file_for_lab2.txt

Finally its all called from a file in the root of the project called Main.py

