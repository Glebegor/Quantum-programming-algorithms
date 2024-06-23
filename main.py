import Bootstrap

def main():
    config = Bootstrap.Config()
    db = Bootstrap.Db(config=config.ToDict())
    app = Bootstrap.Application(config=config.ToDict(), db=db)
    app.run()

if __name__ == '__main__':
    main()