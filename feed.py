import yaml
import xml.etree.ElementTree as xmlTree

with open('feed.yaml') as yamlFile:
    
    # safe load file
    yamlData = yaml.safe_load(yamlFile)

    websiteUrl = yamlData['website_url']
    
    # create rss element
    rssElement = xmlTree.Element('rss', {'version': '2.0', 'xmlns:itunes': 'www.test.com', 'xmlns:content': 'http://test.org'})
    
    # create subelement
    channelElement = xmlTree.SubElement(rssElement, 'channel')
    
    # add text element to subelement
    xmlTree.SubElement(channelElement, 'title').text = yamlData['title']
    
    for item in yamlData['item']:
        itemElement = xmlTree.SubElement(channelElement, 'item', {'length': item['length']})
        xmlTree.SubElement(itemElement, 'itunes:link', {'href': websiteUrl + item['file']})
        xmlTree.SubElement(itemElement, 'title').text = item['title']
        xmlTree.SubElement(itemElement, 'description').text = item['description']
        xmlTree.SubElement(itemElement, 'published').text = item['published']
        xmlTree.SubElement(itemElement, 'duration').text = item['duration']
        
    
    # generate output
    outputTree = xmlTree.ElementTree(rssElement)
    
    # write file
    outputTree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)