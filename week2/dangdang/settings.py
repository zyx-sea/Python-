# Obey robots.txt rules

ROBOTSTXT_OBEY = False

#然后，我们再将配置文件settings.py的pipelines配置部分设置为如下所示，开启对应的pipelines:

# Configure item pipelines

# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html

ITEM_PIPELINES = {

    'dangdang.pipelines.DangdangPipeline': 300,

}