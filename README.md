# 汉字姓氏及罗马标注（拼音）语料

[English Version](./README_EN.md)

语料库包括509个中文姓氏，以及其对应的罗马拼音，格式为Json，每一个汉字姓氏包括以下国家或地区的罗马标注（拼音）用法：

- 简体中文（汉字字符）
- 繁体中文（汉字字符）
- 大陆拼音(罗马字母标注)
- 香港拼音(罗马字母标注)
- 台湾拼音(罗马字母标注)
- 澳门拼音(罗马字母标注)
- 新加坡拼音(罗马字母标注)
- 马来西亚拼音(罗马字母标注)
- 越南拼音(罗马字母标注)
- 韩国拼音(罗马字母标注)

吴语，客家话，闽南语，日语，朝鲜语（北朝鲜），日本语等语言或方言也有不同的拼写方法或是罗马字母标注，由于使用频率较少或只有较少姓氏有对应的中文汉字，故未收集整理。Wiki 有对方言的表格，可以查看。

[wiki](https://en.wikipedia.org/wiki/List_of_common_Chinese_surnames)

每个姓氏整理的格式如下

```jsx
{
	'No.': '8', 
	'zh_sim': '王', 
	'zh_tra': '王', 
	'mainland': 'Wang', 
	'taiwan': 'Wang', 
	'hongkong': 'Wong', 
	'macao': 'Vong/Wong', 
	'singapore': 'Ong/Heng/Wong/Wang', 
	'malaysia': 'Ong/Heng/Wong/Wang/Bong/Ng', 
	'vietname': 'Vương', 
	'Korea': 'Wang'
}
```
