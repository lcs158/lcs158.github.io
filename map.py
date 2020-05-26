# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyecharts
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple xlrd
from pyecharts import options as opts
from pyecharts.charts import Map,Timeline
from pyecharts.charts import Page
from pyecharts.charts import Bar
from pyecharts.charts import MapGlobe    #预留升级成球形地图
from pyecharts.charts import Tab
import pandas as pd
from pyecharts.components import Table
import numpy as np
from pyecharts.options import ComponentTitleOpts

#编写时间：2020年3月8日—3月18日
#编写人：子悠爸爸（广东省土地调查规划院），刘子悠（海珠区实验小学）
#指导老师：梁戈老师（海珠区实验小学）
#解决问题：通过专题地图和专题统计图反映世界各国疫情扩散情况
#解决思路：python+pyecharts+pandas+数据库->html
#数据来源：BAIDU+WHO
#数据库：采用EXCEL
#编程工具：Python IDLE3.6.5，pyecharts1.7.0
#还需要进一步研究MapGlobe，Page与Tab的整合，文字与图片的加入等。
#感谢学校提供了一个良好的平台和机会，感谢梁戈老师细心指导，感谢子悠妈妈理解与支持（虽然我两周没有刮胡子了）。


#国家中英文对照表，引用网上资源，做大幅度修改补充,原来想做成json文件导入，但存在BOM，失败。子悠爸爸
dict1={
    'Afghanistan':'阿富汗',
    'Singapore':'新加坡',
    'Angola':'安哥拉',
    'Albania':'阿尔巴尼亚',
    'United Arab Emirates':'阿拉伯联合酋长国',
    'Argentina':'阿根廷',
    'Armenia':'亚美尼亚',
    'French Southern and Antarctic Lands':'法属南半球和南极领地',
    'Australia':'澳大利亚',
    'Austria':'奥地利',
    'Azerbaijan':'阿塞拜疆',
    'Burundi':'布隆迪',
    'Belgium':'比利时',
    'Benin':'贝宁',
    'Bahrain':'巴林',
    'Burkina Faso':'布基纳法索',
    'Bangladesh':'孟加拉国',
    'Bulgaria':'保加利亚',
    'Bahamas':'巴哈马',
    'Bosnia and Herz.':'波黑',
    'Belarus':'白俄罗斯',
    'Belize':'伯利兹',
    'Bermuda':'百慕大',
    'Bolivia':'玻利维亚',
    'Brazil':'巴西',
    'Brunei':'文莱',
    'Bhutan':'不丹',
    'Botswana':'博茨瓦纳',
    'Central African Rep.':'中非',
    'Canada':'加拿大',
    'Cape Verde':'佛得角',
    'Switzerland':'瑞士',
    'Chile':'智利',
    'China':'中国',
    "Côte d'Ivoire":'科特迪瓦',
    'Cameroon':'喀麦隆',
    'Dem. Rep. Congo':'刚果（金）',
    'Congo':'刚果（布）',
    'Colombia':'哥伦比亚',
    'Costa Rica':'哥斯达黎加',
    'Cuba':'古巴',
    'N. Cyprus':'北塞浦路斯',
    'Cyprus':'塞浦路斯',
    'Czech Rep.':'捷克',
    'Germany':'德国',
    'Djibouti':'吉布提',
    'Denmark':'丹麦',
    'Dominican Rep.':'多米尼加',
    'Algeria':'阿尔及利亚',
    'Ecuador':'厄瓜多尔',
    'Egypt':'埃及',
    'Eritrea':'厄立特里亚',
    'Spain':'西班牙',
    'Estonia':'爱沙尼亚',
    'Ethiopia':'埃塞俄比亚',
    'Finland':'芬兰',
    'Fiji':'斐济',
    'Falkland Islands':'福克兰群岛',
    'France':'法国',
    'Gabon':'加蓬',
    'United Kingdom':'英国',
    'Georgia':'格鲁吉亚',
    'Ghana':'加纳',
    'Guinea':'几内亚',
    'Gambia':'冈比亚',
    'Guinea-Bissau':'几内亚比绍',
    'Eq. Guinea':'赤道几内亚',
    'Greece':'希腊',
    'Greenland':'格陵兰',
    'Guatemala':'危地马拉',
    'French Guiana':'法属圭亚那',
    'Guyana':'圭亚那',
    'Honduras':'洪都拉斯',
    'Croatia':'克罗地亚',
    'Haiti':'海地',
    'Hungary':'匈牙利',
    'Indonesia':'印度尼西亚',
    'India':'印度',
    'Ireland':'爱尔兰',
    'Iran':'伊朗',
    'Iraq':'伊拉克',
    'Iceland':'冰岛',
    'Israel':'以色列',
    'Italy':'意大利',
    'Jamaica':'牙买加',
    'Jordan':'约旦',
    'Japan':'日本',
    'Kazakhstan':'哈萨克斯坦',
    'Kenya':'肯尼亚',
    'Kyrgyzstan':'吉尔吉斯斯坦',
    'Cambodia':'柬埔寨',
    'Korea':'韩国',
    'Kosovo':'科索沃',
    'Kuwait':'科威特',
    'Lao PDR':'老挝',
    'Lebanon':'黎巴嫩',
    'Liberia':'利比里亚',
    'Libya':'利比亚',
    'Sri Lanka':'斯里兰卡',
    'Lesotho':'莱索托',
    'Lithuania':'立陶宛',
    'Luxembourg':'卢森堡',
    'Latvia':'拉脱维亚',
    'Morocco':'摩洛哥',
    'Moldova':'摩尔多瓦',
    'Madagascar':'马达加斯加',
    'Mexico':'墨西哥',
    'Macedonia':'北马其顿',
    'Mali':'马里',
    'Myanmar':'缅甸',
    'Montenegro':'黑山',
    'Mongolia':'蒙古',
    'Mozambique':'莫桑比克',
    'Mauritania':'毛里塔尼亚',
    'Mauritius':'毛里求斯',
    'Malawi':'马拉维',
    'Malta':'马耳他',
    'Malaysia':'马来西亚',
    'Namibia':'纳米比亚',
    'New Caledonia':'新喀里多尼亚',
    'Niger':'尼日尔',
    'Nigeria':'尼日利亚',
    'Nicaragua':'尼加拉瓜',
    'Netherlands':'荷兰',
    'Norway':'挪威',
    'Nepal':'尼泊尔',
    'New Zealand':'新西兰',
    'Oman':'阿曼',
    'Pakistan':'巴基斯坦',
    'Palestine':'巴勒斯坦',
    'Panama':'巴拿马',
    'Peru':'秘鲁',
    'Philippines':'菲律宾',
    'Papua New Guinea':'巴布亚新几内亚',
    'Poland':'波兰',
    'Puerto Rico':'波多黎各',
    'Dem. Rep. Korea':'朝鲜',
    'Portugal':'葡萄牙',
    'Paraguay':'巴拉圭',
    'Qatar':'卡塔尔',
    'Romania':'罗马尼亚',
    'Russia':'俄罗斯',
    'Rwanda':'卢旺达',
    'W. Sahara':'西撒哈拉',
    'Saudi Arabia':'沙特阿拉伯',
    'Sudan':'苏丹',
    'S. Sudan':'南苏丹',
    'Senegal':'塞内加尔',
    'Solomon Islands':'所罗门群岛',
    'Sierra Leone':'塞拉利昂',
    'El Salvador':'萨尔瓦多',
    'Somaliland':'索马里兰',
    'Somalia':'索马里',
    'Serbia':'塞尔维亚',
    'Suriname':'苏里南',
    'Slovakia':'斯洛伐克',
    'Slovenia':'斯洛文尼亚',
    'Sweden':'瑞典',
    'Swaziland':'斯威士兰',
    'Syria':'叙利亚',
    'Chad':'乍得',
    'Togo':'多哥',
    'Thailand':'泰国',
    'Tajikistan':'塔吉克斯坦',
    'Turkmenistan':'土库曼斯坦',
    'East Timor':'东帝汶',
    'Trinidad and Tobago':'特里尼达和多巴哥',
    'Tunisia':'突尼斯',
    'Turkey':'土耳其',
    'Tanzania':'坦桑尼亚',
    'Uganda':'乌干达',
    'Ukraine':'乌克兰',
    'Uruguay':'乌拉圭',
    'United States':'美国',
    'Uzbekistan':'乌兹别克斯坦',
    'Venezuela':'委内瑞拉',
    'Vietnam':'越南',
    'Vanuatu':'瓦努阿图',
    'West Bank':'西岸',
    'Yemen':'也门',
    'South Africa':'南非',
    'Zambia':'赞比亚',
    'Zimbabwe':'津巴布韦',
    'Cayman Is.':'开曼群岛',
    'Antigua and Barb.':'安提瓜和巴布达',
    'Dominica':'多米尼克',
    'Saint Lucia':'圣卢西亚',
    'St. Vin. and Gren.':'圣文森特',
    'Barbados':'巴巴多斯',
    'Grenada':'格林纳达',
    'U.S. Virgin Is.':'美属维尔京群岛',
    'Montserrat':'圣基茨和尼维斯',
    'Curaçao':'库拉索（荷）',
    'São Tomé and Principe':'圣多美和普林西比',
    'Comoros':'科摩罗',
    'Fr. S. Antarctic Lands':'凯尔盖朗岛',
    'Heard I. and McDonald Is.':'赫德岛',
    'Solomon Is.':'所罗门群岛',
    'Palau':'帕劳',
    'Micronesia':'密克罗尼西亚',
    'Guam':'关岛（美）',
    'N. Mariana Is.':'北马里亚纳群岛（美）',
    'Falkland Is.':'马尔维纳斯群岛（阿、英）',
    'S. Geo. and S. Sandw. Is':'南乔治亚岛',
    'Tonga':'汤加',
    'Samoa':'萨摩亚',
    'Fr. Polynesia':'法属波利尼西亚',
    'Faeroe Is.':'法罗群岛',
    'Timor-Leste':'东帝汶',
    'Liechtenstein':'列支敦士登',
    'Andorra':'安道尔',
    'Seychelles':'塞舌尔'
}


#读取EXCEL疫情数据库，来源于百度和世界卫生组织报告，数据库由刘子悠和子悠爸爸共同建立，其中疫情数据主要由刘子悠录入，爸爸负责数据结构与质量审核

df = pd.read_excel("疫情数据库.xlsx","Sheet1",encoding = "utf-8")

#解析列数据
gj = df['国家']
rk = df["人口"]
ljzy=df['0315累计治愈'].fillna(value=0)
ljsw=df['0315累计死亡'].fillna(value=0)
ljqz=df['0315累计确诊']
ljqz8=df['0308累计确诊']
ljqz9=df['0309累计确诊']
ljqz10=df['0310累计确诊']
ljqz11=df['0311累计确诊']
ljqz12=df['0312累计确诊']
ljqz13=df['0313累计确诊']
ljqz14=df['0314累计确诊']

#列数据转数组
gjs=[str(gj[i]) for i in range(len(gj))]

rks=[rk[i] for i in range(len(gj))]

ljqzs=[ljqz[i]  for i in range(len(ljqz))]

pcolor =['#FFFFCC','#CCFFFF','#99CCFF','#66CCFF','#0099CC','#0066CC','#333399']  #子悠配色数组

#地图1：各国现存病例专题图（静态地图模板），子悠爸爸
rkdata = [[gj[i], (ljqz[i]-ljsw[i]-ljzy[i])] for i in range(len(gj))]                #第一步，导入存量病例数据（把大象拿过来）

rkmap = (
    Map()                                                                            #第二步，引入地图模板，设置标题和数据分组（把冰箱打开）
     .set_global_opts(title_opts=opts.TitleOpts(title="截至2020年3月15日，各国现存病例人数"),
                     visualmap_opts=opts.VisualMapOpts(range_color=pcolor,split_number=6,is_piecewise=True,
                                                       pieces=[{"min": 10000},
                                                           {"min": 5000, "max": 10000},
                                                           {"min": 1000, "max": 5000},
                                                           {"min": 100, "max": 1000},
                                                           {"min": 10, "max": 100},
                                                           {"max": 10},]
                                                           ))
    .add("现存病例", rkdata, maptype="world",name_map=dict1,is_map_symbol_show=False) #第三步，把数据灌进地图（把大象塞进冰箱）
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
)




#尝试制作时间线地图，引用二维数组作为动态数据，并替换原有静态数据，子悠爸爸
tl=Timeline()

qzndata=[[[gj[i], ljqz8[i]] for i in range(len(gj))],
         [[gj[i], ljqz9[i]] for i in range(len(gj))],
         [[gj[i], ljqz10[i]] for i in range(len(gj))],
         [[gj[i], ljqz11[i]] for i in range(len(gj))],
         [[gj[i], ljqz12[i]] for i in range(len(gj))],
         [[gj[i], ljqz13[i]] for i in range(len(gj))],
         [[gj[i], ljqz14[i]] for i in range(len(gj))],
         [[gj[i], ljqz[i]] for i in range(len(gj))]
         ]

#地图2：世界累计确珍专题图，刘子悠
qzdata = [[gj[i], ljqz[i]] for i in range(len(gj))]  #静态数据
lzycolor=['#FFFFCC','#CCFFFF','#99CCFF','#66CCFF','#0099CC','#0066CC','#333399']  #配色组合，刘子悠，颜色值来源于http://tool.chinaz.com/tools/use
for i in range(0, 8):
    qznmap = (
        Map()
        .set_global_opts(title_opts=opts.TitleOpts(title="2020年3月{}日各国累计确诊情况，LZY".format(i+8)),
                     visualmap_opts=opts.VisualMapOpts(range_color=lzycolor,split_number=7,is_piecewise=True,
                                                       pieces=[{"min": 15000},
                                                               {"min": 10000, "max": 15000},
                                                               {"min": 5000, "max": 10000},
                                                               {"min": 1000, "max": 5000},
                                                               {"min": 100, "max": 1000},
                                                               {"min": 10, "max": 100},
                                                               {"max": 10},]
                                                               ))
    .add("感染人数", qzndata[i], maptype="world",name_map=dict1,is_map_symbol_show=False)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )
    tl.add(qznmap,'3月{}日'.format(i+8))




#替换二维数组，改用时间线地图，子悠爸爸

tlgr=Timeline()

grndata=[[[gj[i], round(ljqz8[i]*10000/rk[i],2)] for i in range(len(gj))],
         [[gj[i], round(ljqz9[i]*10000/rk[i],2)] for i in range(len(gj))],
         [[gj[i], round(ljqz10[i]*10000/rk[i],2)] for i in range(len(gj))],
         [[gj[i], round(ljqz11[i]*10000/rk[i],2)] for i in range(len(gj))],
         [[gj[i], round(ljqz12[i]*10000/rk[i],2)] for i in range(len(gj))],
         [[gj[i], round(ljqz13[i]*10000/rk[i],2)] for i in range(len(gj))],
         [[gj[i], round(ljqz14[i]*10000/rk[i],2)] for i in range(len(gj))],
         [[gj[i], round(ljqz[i]*10000/rk[i],2)] for i in range(len(gj))]
         ]
#地图3：世界感染率专题图（每千万人中被感染人数），刘子悠，
for i in range(0,8):
    grnmap = (
       Map()
        .set_global_opts(title_opts=opts.TitleOpts(title="2020年3月{}日各国感染指数（病例数/千万人）".format(i+8)),
                     visualmap_opts=opts.VisualMapOpts(range_color=lzycolor,split_number=7,is_piecewise=True,
                                                       pieces=[{"min": 1500},
                                                               {"min": 1000, "max": 1500},
                                                               {"min": 500, "max": 1000},
                                                               {"min": 100, "max": 500},
                                                               {"min": 10, "max": 100},
                                                               {"min": 1, "max": 10},
                                                               {"max": 1},]
                                                           ))
    .add("感染指数", grndata[i], maptype="world",name_map=dict1,is_map_symbol_show=False)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )
    tlgr.add(grnmap,'3月{}日'.format(i+8))



    
#条型图1：输入性风险评估
#评估指数=3*(确诊增长率/MAX(各国确诊增长率)+2*(所在国华人数/MAX(各国华人数))+5*(确诊人数/MAX(各国确诊人数))
df2 = pd.read_excel("疫情数据库.xlsx","Sheet4",encoding = "utf-8")
topg = df2['国家']
srzs = df2["输入性风险"]
topgs=[topg[i] for i in range(len(topg))]
srzss=[round(srzs[i],2) for i in range(len(topg))]

wbar = (
    Bar()
    .add_xaxis(topgs)
    .add_yaxis('风险指数（3月15日）',srzss)
    .set_global_opts(title_opts={"text":"输入性风险评估（确诊人数超过1000的国家）",
                                 "subtext":"输入性风险主要考虑三个因素，第一是确诊人数，第二是增长速度，第三是该国华人人数，采用综合权重打分法，理论最高为10分。具体数据和算法见疫情数据库。"})
)



#插入表格,子悠爸爸。Pyecharts官网上（http://pyecharts.org/）记录表格和照片与Page不兼容，但经测试，表格可以很好的与Page融合

#表格1：累计确诊前十名的国家
qztab = Table()
df.sort_values(by=["0315累计确诊"],ascending=False) #数据库排序

headers = [df['国家'][i] for i in range(0,10)]
rows = [[df["0315累计确诊"][i] for i in range(0,10)]]

qztab.add(headers, rows)
qztab.set_global_opts(title_opts=ComponentTitleOpts(title="全球新冠肺炎累计确诊病例前十国家", subtitle="截至2020年3月15日"))


#表格2：累计感染率前十名的国家
grltab=Table()

c=[[gj[i], round(ljqz[i]*10000/rk[i],2)] for i in range(len(gj)) if ljqz[i]>9]

grdata=sorted(c,key=lambda x:x[1],reverse=True)  #数组重新排序

cheaders = [grdata[i][0] for i in range(0,10)]
crows = [[grdata[i][1] for i in range(0,10)]]

grltab.add(cheaders, crows)
grltab.set_global_opts(title_opts=ComponentTitleOpts(title="全球新冠肺炎感染率前十国家(每千万人中感染人数)", subtitle="截至2020年3月15日"))


#页面布局组合
page=Page(layout=Page.SimplePageLayout)
page=Page(page_title="全球COVID19疫情扩散与输入性风险分析—海珠实验小学六年四班刘子悠的研学作品")

page.add(rkmap)
page.add(qztab)
page.add(tl)
page.add(grltab)
page.add(tlgr)
page.add(wbar)

#mtab=Tab() Tab与Page不兼容，忍痛放弃
#mtab=Tab(page_title="刘子悠的研学作品-tab")
#mtab.render("mytabmaps.html"),template_name='simple_page.html'

page.render('index2.html')







