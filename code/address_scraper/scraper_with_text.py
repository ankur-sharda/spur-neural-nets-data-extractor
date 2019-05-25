from address_scraper.data import Data
from address_scraper.page_data import PageData
from address_scraper.encoding import Encoding
from address_scraper.dictionary import Dictionary
from address_scraper.neural_network import NeuralNetwork


class Scraper:

    training_addresses = Data().load_addresses("US", "TX")
    training_addresses.extend(Data().load_addresses("US", "AL"))
    training_texts = PageData().read_and_process_webpage(
        "https://holocrontoystore.com/collections/graded-figures-modern/products/40th-han-solo-afa8-5-2873029", 20)
    training_texts.extend(PageData().read_and_process_webpage(
        "https://holocrontoystore.com/collections/a-new-hope/products/bs6-63-grand-moff-tarkin", 20))
    training_texts.extend(PageData().read_and_process_webpage(
        "https://holocrontoystore.com/collections/30th-anniversary/products/concept-stormtrooper-30th", 20))
    training_texts.extend(PageData().read_and_process_webpage(
        "https://holocrontoystore.com/collections/30th-anniversary/products/cz-4-26-30th-rotj-2007", 20))
    training_texts.extend(PageData().read_and_process_webpage(
        "https://holocrontoystore.com/collections/30th-anniversary/products/darth-vader-concept-28-30th-signature-series-2007", 20))
    training_texts.extend(PageData().read_and_process_webpage(
        "https://holocrontoystore.com/collections/black-series-2013-2018/products/bs-tiny-porg", 20))
    training_texts.extend(PageData().read_and_process_webpage(
        "https://holocrontoystore.com/collections/a-new-hope/products/40th-chewbacca", 20))
    training_texts.extend(PageData().read_and_process_webpage(
        "https://holocrontoystore.com/collections/a-new-hope/products/40th-han-solo", 20))
    training_texts.extend(PageData().read_and_process_webpage(
        "https://holocrontoystore.com/collections/a-new-hope/products/40th-sand-people-tusken-raider-2017", 20))
    training_texts.extend(PageData().read_and_process_webpage(
        "https://holocrontoystore.com/collections/30th-anniversary/products/r2-d2-and-c-3po-concept-30th-signature-series-2007", 20))
    training_texts.extend(PageData().read_and_process_webpage(
        "https://holocrontoystore.com/collections/30th-anniversary/products/covert-ops-clone-trooper-30th-saga-legends-2007", 20))
    training_texts.extend(PageData().read_and_process_webpage("https://www.fantasyislandtoys.com/shop/index.php", 20))
    training_texts.extend(PageData().read_and_process_webpage("https://www.fantasyislandtoys.com/shop/index.php?l=product_list&c=134", 20))
    training_texts.extend(PageData().read_and_process_webpage("https://www.fantasyislandtoys.com/shop/index.php?l=page_view&p=gift_certificates", 20))
    training_texts.extend(PageData().read_and_process_webpage("https://www.fantasyislandtoys.com/shop/index.php?l=product_list&c=96", 20))
    training_texts.extend(PageData().read_and_process_webpage("https://www.fantasyislandtoys.com/shop/index.php?l=product_detail&p=48403568", 20))
    training_texts.extend(PageData().read_and_process_webpage("https://www.fantasyislandtoys.com/shop/index.php?l=product_detail&p=48407755", 20))
    training_texts.extend(PageData().read_and_process_webpage("https://www.fantasyislandtoys.com/shop/index.php?l=product_detail&p=48407589", 20))

    # predict_addresses = Data().load_addresses("US", "WY")
    predict_texts = PageData().read_and_process_webpage(
        "https://holocrontoystore.com/collections/a-new-hope/products/bs6-63-grand-moff-tarkin", 20)
    predict_texts = PageData().read_and_process_webpage("https://oakmountainhobbies.com/", 20)

    dict = Dictionary("dict")
    dict.build(training_addresses)
    dict.build(training_texts)
    print(">>", len(training_addresses), len(training_texts))
    # dict.build(predict_addresses)
    dict.build(predict_texts)
    # print(">>", len(predict_addresses), len(predict_texts))
    dict.save()

    print(dict.data)
    print(len(dict.data))

    # ------------------------------------------------------------------------------------------------------------------

    enc1 = Encoding("address_training_encodings")
    training_encodings = enc1.encode_list(dict, training_addresses)

    enc2 = Encoding("text_training_encodings")
    training_encodings.extend(enc2.encode_texts(dict, training_texts))

    encToSave = Encoding("training_encodings")
    encToSave.save(training_encodings)

    # # ------------------------------------------------------------------------------------------------------------------

    enc3 = Encoding("text_predict_encodings")

    predict_encodings = []
    # predict_encodings = enc3.encode_list(dict, predict_addresses)
    predict_encodings.extend(enc3.encode_texts(dict, predict_texts))

    encToSavePr = Encoding("predict_encodings")
    encToSavePr.save(predict_encodings)

    # # ------------------------------------------------------------------------------------------------------------------

    nn = NeuralNetwork()
    nn.train("training_encodings", 1)
    nn.predict("predict_encodings", 0)

