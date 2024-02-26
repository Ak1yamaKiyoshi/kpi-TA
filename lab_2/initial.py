
from Graph import Graph


places = [
    "Червоний університет",
    "Андріївська церква",
    "Михайлівський собор",
    "Золоті ворота",
    "Лядські ворота",
    "Фунікулер",
    "Київська політехніка",
    "Фонтан на Хрещатику",
    "Софія київська",
    "Національна філармонія",
    "Музей однієї вулиці",
    "Гуртожиток НТУУ КПІ"
]

kyiv_map = Graph()
for place in places:
    kyiv_map.add_node(place)

#! Перед здачею відредагувати, та видалити 
## ті сполучення, яких немає
## 

kyiv_map.add_edge(kyiv_map["Червоний університет"], kyiv_map["Михайлівський собор"], distance=2)
kyiv_map.add_edge(kyiv_map["Червоний університет"], kyiv_map["Золоті ворота"], distance=3)
kyiv_map.add_edge(kyiv_map["Червоний університет"], kyiv_map["Лядські ворота"], distance=4)
kyiv_map.add_edge(kyiv_map["Червоний університет"], kyiv_map["Фунікулер"], distance=5)
kyiv_map.add_edge(kyiv_map["Червоний університет"], kyiv_map["Київська політехніка"], distance=6)
kyiv_map.add_edge(kyiv_map["Червоний університет"], kyiv_map["Фонтан на Хрещатику"], distance=7)
kyiv_map.add_edge(kyiv_map["Червоний університет"], kyiv_map["Софія київська"], distance=8)
kyiv_map.add_edge(kyiv_map["Червоний університет"], kyiv_map["Національна філармонія"], distance=9)
kyiv_map.add_edge(kyiv_map["Червоний університет"], kyiv_map["Музей однієї вулиці"], distance=10)
kyiv_map.add_edge(kyiv_map["Червоний університет"], kyiv_map["Гуртожиток НТУУ КПІ"], distance=11)
kyiv_map.add_edge(kyiv_map["Михайлівський собор"], kyiv_map["Андріївська церква"], distance=2)
kyiv_map.add_edge(kyiv_map["Михайлівський собор"], kyiv_map["Золоті ворота"], distance=3)
kyiv_map.add_edge(kyiv_map["Михайлівський собор"], kyiv_map["Лядські ворота"], distance=4)
kyiv_map.add_edge(kyiv_map["Михайлівський собор"], kyiv_map["Фунікулер"], distance=5)
kyiv_map.add_edge(kyiv_map["Михайлівський собор"], kyiv_map["Київська політехніка"], distance=6)
kyiv_map.add_edge(kyiv_map["Михайлівський собор"], kyiv_map["Фонтан на Хрещатику"], distance=7)
kyiv_map.add_edge(kyiv_map["Михайлівський собор"], kyiv_map["Софія київська"], distance=8)
kyiv_map.add_edge(kyiv_map["Михайлівський собор"], kyiv_map["Національна філармонія"], distance=9)
kyiv_map.add_edge(kyiv_map["Михайлівський собор"], kyiv_map["Музей однієї вулиці"], distance=10)
kyiv_map.add_edge(kyiv_map["Михайлівський собор"], kyiv_map["Гуртожиток НТУУ КПІ"], distance=11)
kyiv_map.add_edge(kyiv_map["Золоті ворота"], kyiv_map["Лядські ворота"], distance=2)
kyiv_map.add_edge(kyiv_map["Золоті ворота"], kyiv_map["Фунікулер"], distance=3)
kyiv_map.add_edge(kyiv_map["Золоті ворота"], kyiv_map["Київська політехніка"], distance=4)
kyiv_map.add_edge(kyiv_map["Золоті ворота"], kyiv_map["Фонтан на Хрещатику"], distance=5)
kyiv_map.add_edge(kyiv_map["Золоті ворота"], kyiv_map["Софія київська"], distance=6)
kyiv_map.add_edge(kyiv_map["Золоті ворота"], kyiv_map["Національна філармонія"], distance=7)
kyiv_map.add_edge(kyiv_map["Золоті ворота"], kyiv_map["Музей однієї вулиці"], distance=8)
kyiv_map.add_edge(kyiv_map["Золоті ворота"], kyiv_map["Гуртожиток НТУУ КПІ"], distance=9)
kyiv_map.add_edge(kyiv_map["Лядські ворота"], kyiv_map["Фунікулер"], distance=2)
kyiv_map.add_edge(kyiv_map["Лядські ворота"], kyiv_map["Київська політехніка"], distance=3)
kyiv_map.add_edge(kyiv_map["Лядські ворота"], kyiv_map["Фонтан на Хрещатику"], distance=4)
kyiv_map.add_edge(kyiv_map["Лядські ворота"], kyiv_map["Софія київська"], distance=5)
kyiv_map.add_edge(kyiv_map["Лядські ворота"], kyiv_map["Національна філармонія"], distance=6)
kyiv_map.add_edge(kyiv_map["Лядські ворота"], kyiv_map["Музей однієї вулиці"], distance=7)
kyiv_map.add_edge(kyiv_map["Лядські ворота"], kyiv_map["Гуртожиток НТУУ КПІ"], distance=8)
kyiv_map.add_edge(kyiv_map["Фунікулер"], kyiv_map["Київська політехніка"], distance=2)
kyiv_map.add_edge(kyiv_map["Фунікулер"], kyiv_map["Софія київська"], distance=3)
kyiv_map.add_edge(kyiv_map["Фунікулер"], kyiv_map["Національна філармонія"], distance=4)
kyiv_map.add_edge(kyiv_map["Фунікулер"], kyiv_map["Музей однієї вулиці"], distance=5)
kyiv_map.add_edge(kyiv_map["Фунікулер"], kyiv_map["Гуртожиток НТУУ КПІ"], distance=6)
kyiv_map.add_edge(kyiv_map["Київська політехніка"], kyiv_map["Фонтан на Хрещатику"], distance=2)
kyiv_map.add_edge(kyiv_map["Київська політехніка"], kyiv_map["Софія київська"], distance=3)
kyiv_map.add_edge(kyiv_map["Київська політехніка"], kyiv_map["Національна філармонія"], distance=4)
kyiv_map.add_edge(kyiv_map["Київська політехніка"], kyiv_map["Музей однієї вулиці"], distance=5)
kyiv_map.add_edge(kyiv_map["Київська політехніка"], kyiv_map["Гуртожиток НТУУ КПІ"], distance=6)
kyiv_map.add_edge(kyiv_map["Фонтан на Хрещатику"], kyiv_map["Софія київська"], distance=2)
kyiv_map.add_edge(kyiv_map["Фонтан на Хрещатику"], kyiv_map["Національна філармонія"], distance=3)
kyiv_map.add_edge(kyiv_map["Фонтан на Хрещатику"], kyiv_map["Музей однієї вулиці"], distance=4)
kyiv_map.add_edge(kyiv_map["Фонтан на Хрещатику"], kyiv_map["Гуртожиток НТУУ КПІ"], distance=5)
kyiv_map.add_edge(kyiv_map["Софія київська"], kyiv_map["Національна філармонія"], distance=2)
kyiv_map.add_edge(kyiv_map["Софія київська"], kyiv_map["Музей однієї вулиці"], distance=3)
kyiv_map.add_edge(kyiv_map["Софія київська"], kyiv_map["Гуртожиток НТУУ КПІ"], distance=4)
kyiv_map.add_edge(kyiv_map["Національна філармонія"], kyiv_map["Музей однієї вулиці"], distance=2)
kyiv_map.add_edge(kyiv_map["Національна філармонія"], kyiv_map["Гуртожиток НТУУ КПІ"], distance=3)
kyiv_map.add_edge(kyiv_map["Музей однієї вулиці"], kyiv_map["Гуртожиток НТУУ КПІ"], distance=2)
kyiv_map.add_edge(kyiv_map["Андріївська церква"], kyiv_map["Лядські ворота"], distance=3)
kyiv_map.add_edge(kyiv_map["Андріївська церква"], kyiv_map["Фунікулер"], distance=4)
kyiv_map.add_edge(kyiv_map["Андріївська церква"], kyiv_map["Київська політехніка"], distance=5)
kyiv_map.add_edge(kyiv_map["Андріївська церква"], kyiv_map["Фонтан на Хрещатику"], distance=6)
kyiv_map.add_edge(kyiv_map["Андріївська церква"], kyiv_map["Софія київська"], distance=7)
kyiv_map.add_edge(kyiv_map["Андріївська церква"], kyiv_map["Національна філармонія"], distance=8)
kyiv_map.add_edge(kyiv_map["Андріївська церква"], kyiv_map["Музей однієї вулиці"], distance=9)
kyiv_map.add_edge(kyiv_map["Андріївська церква"], kyiv_map["Гуртожиток НТУУ КПІ"], distance=10)
