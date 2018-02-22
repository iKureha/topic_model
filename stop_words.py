# encoding='utf-8'

stop_words = ['this', 'anywhere', 'although', 'ten', 'keep', 'side', 'yet', 'four', 'ie', 'itself', 'same', 'along',
              'enough', 'done', 'forty', 'anyhow', 'she', 'the', 'each', 'twenty', 'fifteen', 'from', 'what', 'besides',
              'before', 'even', 'most', 'thence', 'in', 'see', 'also', 'hereupon', 'they', 'me', 'etc', 'beyond',
              'being', 'myself', 'whole', 'move', 'two', 'three', 'go', 'full', 'con', 'top', 'perhaps', 'less', 'both',
              'describe', 'everywhere', 'former', 'either', 'afterwards', 'anyone', 'one', 'so', 'latterly', 'therein',
              'her', 'mostly', 'seemed', 'still', 'not', 'while', 'whereafter', 'whose', 'everything', 'very', 'at', 'to',
              'another', 'until', 'why', 'since', 'thereafter', 'as', 'ltd', 'call', 'than', 'without', 'up', 'alone',
              'many', 'mill', 'cry', 'such', 'too', 'un', 'whence', 'eleven', 'nobody', 'whenever', 'became', 'fifty',
              'can', 'cannot', 'empty', 'he', 'meanwhile', 'do', 'somehow', 'onto', 'whether', 'you', 'how', 'thus',
              'made', 'during', 'on', 'over', 'was', 'down', 'ever', 'namely', 'own', 'system', 'hers', 'therefore',
              'together', 'were', 'almost', 'inc', 'some', 'already', 'where', 'others', 'sixty', 'amount', 'latter',
              'throughout', 'please', 'us', 'we', 'are', 'due', 'more', 'third', 'else', 'who', 'our', 'but', 'ourselves',
              'co', 'hereby', 'nine', 'put', 'between', 'there', 'which', 'into', 'because', 'rather', 'would', 'part',
              'nor', 'yourself', 'must', 'nowhere', 'his', 'or', 'cant', 'whereby', 'within', 'among', 'bottom', 'indeed',
              'seem', 'thick', 'through', 'may', 'herself', 'sometime', 'anyway', 'seems', 'towards', 'an', 'with',
              'am', 'their', 'sincere', 'take', 'though', 'yourselves', 'eg', 'however', 'per', 'been', 'something',
              'via', 'few', 'if', 'thru', 'could', 'thereupon', 'every', 'much', 'get', 'around', 'whereas', 'those',
              'be', 'hundred', 'whereupon', 'any', 'themselves', 'under', 'except', 'about', 'eight', 'nothing', 'off',
              'upon', 'of', 'again', 'wherever', 'becomes', 'herein', 'amongst', 'below', 'now', 'several', 'further',
              'my', 'formerly', 'wherein', 'after', 'ours', 'elsewhere', 'all', 'twelve', 'mine', 'nevertheless', 'its',
              'anything', 'might', 'once', 'him', 'de', 'no', 'other', 'seeming', 'them', 'five', 'least', 'amoungst',
              'becoming', 'none', 'will', 'whoever', 'bill', 'it', 'whom', 'somewhere', 'when', 'couldnt', 'neither',
              'show', 'thereby', 'last', 'often', 'sometimes', 'become', 'well', 'interest', 'back', 'serious', 'above',
              'against', 'and', 'fill', 'front', 'here', 'is', 'first', 'detail', 'i', 'hasnt', 'then', 'give', 'moreover',
              'out', 'that', 'noone', 'toward', 'found', 'name', 'whatever', 'had', 'someone', 'yours', 'a', 'otherwise',
              'beside', 'thin', 'fire', 'always', 'beforehand', 'everyone', 'have', 'only', 'across', 'behind', 'for', 'by',
              'hereafter', 'six', 'never', 'should', 'these', 'your', 're', 'find', 'himself', 'has', 'whither', 'next',
              'hence', 'rt', 'lmao', 'lol', 'xD', 'https', 'http', 'click', 'ins', 'here', 'sorry', 'thanks', 'hi', 'help',
              'today', 'yesterday', 'good', 'share', 'time', 'day', 'thank', 'new', 'subscribe', 'follow', 'submit',
              'feedback', 'hear', 'support', 'amp', 'think', 'just', 'luck', 'lucky', 'send', 'let', 'know', 'love', 'try',
              'la', 'el', 'en', 'ya', 'yep', 'nope', 'al']
print(len(stop_words))