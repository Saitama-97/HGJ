import numpy as np
import os
import matplotlib.pyplot as plt

cls_num = 8
f1 = open('/Users/Saitama/PycharmProjects/HGJ/Code/Txts/label.txt', 'r')
# f1 = open('/Users/Saitama/PycharmProjects/HGJ/Code/label.txt', 'r')
labels = []
for c in f1:
    for i in c:
        if i != ' ':
            # print(i)
            labels.append(int(i))
print(len(labels))

f2 = open('/Users/Saitama/PycharmProjects/HGJ/Code/Txts/pred.txt', 'r')
# f2 = open('/Users/Saitama/PycharmProjects/HGJ/Code/pred.txt', 'r')
predicted = []
for c in f2:
    for i in c:
        if i != ' ':
            # print(i)
            predicted.append(int(i))
print(len(predicted))

# labels = [0, 1, 3, 4, 1, 1, 1, 0, 4, 2]
# predicted = [0, 1, 3, 4, 1, 1, 1, 0, 2, 3]
# 第一步：创建混淆矩阵
# 获取类别数，创建 N*N 的零矩阵
conf_mat = np.zeros([cls_num, cls_num])
# 第二步：获取真实标签和预测标签
# labels 为真实标签，通常为一个 batch 的标签
# predicted 为预测类别，与 labels 同长度
# 第三步：依据标签为混淆矩阵计数
for i in range(len(labels)):
    true_i = np.array(labels[i])
    pre_i = np.array(predicted[i])
    conf_mat[true_i, pre_i] += 1.0
# print(conf_mat)
# ----------------RuntimeWarning: invalid value encountered in true_divide----------#
np.seterr(divide='ignore', invalid='ignore')


def show_confMat(confusion_mat, classes_name, set_name, out_dir):
    """
    可视化混淆矩阵，保存png格式
    :param confusion_mat: nd-array
    :param classes_name: list,各类别名称
    :param set_name: str, eg: 'valid', 'train'
    :param out_dir: str, png输出的文件夹
    :return:
    """
    # 归一化
    confusion_mat_N = confusion_mat.copy()
    for i in range(len(classes_name)):
        confusion_mat_N[i, :] = confusion_mat[i, :] / confusion_mat[i, :].sum()

    # 获取颜色
    cmap = plt.cm.get_cmap('BuPu')  # 更多颜色: http://matplotlib.org/examples/color/colormaps_reference.html
    plt.imshow(confusion_mat_N, cmap=cmap)
    plt.colorbar()

    # 设置文字
    xlocations = np.array(range(len(classes_name)))
    plt.xticks(xlocations, classes_name, fontproperties='Times New Roman', size=9)
    plt.yticks(xlocations, classes_name, fontproperties='Times New Roman', size=10)
    plt.xlabel('Prediction', fontdict={'family': 'Times New Roman', 'size': 13})
    plt.ylabel('Target', fontdict={'family': 'Times New Roman', 'size': 13})
    # plt.title('Confusion_Matrix_' + set_name)
    plt.title('Confusion Matrix Visualization',fontdict={'family' : 'Times New Roman'})

    # 打印数字
    # for i in range(confusion_mat_N.shape[0]):
    #     for j in range(confusion_mat_N.shape[1]):
    #         plt.text(x=j, y=i, s=int(confusion_mat[i, j]), va='center', ha='center', color='red', fontsize=10)
    # 保存
    plt.savefig(os.path.join(out_dir, 'Confusion_Matrix_' + set_name + '.png'))
    plt.close()


# 函数调用示例
show_confMat(conf_mat, ['Neutral', 'Happy', 'Sad', 'Surprise', 'Fear', 'Disgust', 'Anger', 'Contempt'], "train",
             "/Users/Saitama/PycharmProjects/HGJ/Code/Images/")
