from ape import accounts, project


def test_encrypt_decrypt(accounts):

    privateKey = 12
    data = 238774529084732462

    c = project.ECC.deploy(sender=accounts[0])
    c.buildPublicKey(privateKey, sender=accounts[0])
    c.encrypt(data, sender=accounts[0])
    c.decrypt(privateKey, sender=accounts[0])
    assert data == c.decryptedMessage()


def test_encrypt_ext(accounts):
    privateKey = 70207068738744339320790887574594053441270106954726605209985050506315940516732
    data = 238774529084732462

    c = project.ECC.deploy(sender=accounts[0])
    c.buildPublicKey(privateKey, sender=accounts[0])
    output = c.encrypt.call(data, sender=accounts[0])
    print(output[1].x.x)
    print(c.encryptedMessageXX())
    print(c.encryptedMessageXY())
    print(c.encryptedMessageYX())
    print(c.encryptedMessageYY())


def test_key_generation(accounts):
    privateKey = 238432489239

    c = project.ECC.deploy(sender=accounts[0])
    c.buildPublicKey(privateKey, sender=accounts[0])
    print(c.publicKeyX())
    print(c.publicKeyY())
