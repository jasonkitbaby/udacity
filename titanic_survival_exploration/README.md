

# run notebook #
    jupyter notebook titanic_survival_exploration.ipynb


# conver notebook to html #
以在 %matplotlib inline 之后使用 %config InlineBackend.figure_format = 'retina' 来呈现分辨率较高的图像。

    jupyter nbconvert --to html notebook.ipynb


# 运行幻灯片 #

要通过 notebook 文件创建幻灯片，需要使用 nbconvert：

    jupyter nbconvert notebook.ipynb --to slides

这只是将 notebook 转换为幻灯片必需的文件，你需要向其提供 HTTP 服务器才能真正看到演示文稿。

要转换它并立即看到它，请使用

    jupyter nbconvert notebook.ipynb --to slides --post serve
