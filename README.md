# myweb

* 不能以index作为文件夹名哦，不然会和index.html冲突 
* 主目录下不能同时出现index.html和signin。html哦，否侧会导致git actions CI不成功
* startbootstrap-clean-blog-gh-pages---col-xl-7 修改显示宽度

## html 跳转页面，同时跳转到一个指定的位置
* a.html里：

  ```<a href="b.html#abc">xxx</a>```

* b.html里加一个锚记：

  ```<a name="abc"></a>```

* JQuery方法

  ```$("html,body").animate({scrollTop:$("#${nameMao}").offset().top},1000);```
