# Kenzie's 5th Module Final Project  

<!-- https://github.com/kenzie-final-project/kenzie-bookings -->

URLS /api/
login/(POST)

accounts/<pk>(PATCH> nao pode mudar is_host, GET, DELETE)
bookings/ (GET>admin pegar tudo, nao admin pega só os propios bookings)
lodgings/<id_lodgings>/bookings (GET, user normal pega o propio, host pega todos bookings do hotel)
lodgings/<id_lodgings>/rooms/<id_room>/bookings (GET>só o dono do host pode ver, POST)
lodgings/<id_lodgings>/rooms/<id_room>/bookings/<pk> (PATCH,DELETE,GET restrito ao propio book)
lodgings/<id_lodgings>/rooms (GET,POST)
lodgings/<id_lodgings>/rooms/<pk>(PATCH,DELETE,GET)

accounts/ (POST, GET)
lodgings/<id_lodgings>/rooms/<id_room>/reviews(GET,POST> só o usuario que ficou naquele room)
lodgings/<id_lodgings>/rooms/<id_room>/reviews/<pk>(GET,PATCH,DELETE)
lodgings/<id_lodgings>/reviews(GET)
reviews/ (GET, admin pegar tudo, nao admin pega só os propios reviews)
lodgings/(GET,POST)
lodgings/<pk>(GET,PATCH,DELETE)
