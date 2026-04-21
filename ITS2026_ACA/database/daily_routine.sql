{
    "type": "MySQLNotebook",
    "version": "1.0",
    "caption": "Script",
    "content": "# creare utente\nCREATE USER `user`@localhost IDENTIFIED BY 'password';\nCREATE USER its2026@localhost IDENTIFIED BY 'password';\n# creare database\nCREATE DATABASE provamicrofono;\nCREATE DATABASE  its2026;\n\n# assegnare permessi a utente su database\nGRANT ALL on provamicrofono.* TO user@localhost;\nGRANT ALL on its2026.* TO user@localhost;\n\n# connessione da utente a database\n# mysql -u user -p\n\n# creazione di tabella\nCREATE TABLE provamicrofono.citta LIKE world.city;\n\n# inserimento / lettura / modifica / eliminazione record\nINSERT INTO provamicrofono.citta \nSELECT * from world.city;\n\nSELECT * FROM provamicrofono.citta;\nSELECT DISTINCT CountryCode from provamicrofono.citta;\nSELECT * FROM provamicrofono.citta WHERE CountryCode = 'ITA';\nSELECT * FROM provamicrofono.citta WHERE CountryCode = 'ITA' and District = 'Apulia';\nSELECT CountryCode , SUM(population) AS abitanti\nfrom provamicrofono.citta \ngroup by CountryCode\norder by CountryCode asc;\n\n\n# eliminazione tabella\ndrop table provamicrofono.citta;\n\n# revocare privilegi\nrevoke all on provamicrofono.* from user@localhost;\n\n# eliminare database\ndrop DATABASE provamicrofono;\n\n# eliminare utente\nDROP USER user@localhost;\n",
    "options": {
        "tabSize": 4,
        "indentSize": 4,
        "insertSpaces": true,
        "defaultEOL": "LF",
        "trimAutoWhitespace": true
    },
    "viewState": null,
    "contexts": [
        {
            "state": {
                "start": 1,
                "end": 43,
                "language": "mysql",
                "result": {
                    "type": "text",
                    "text": [
                        {
                            "type": 2,
                            "index": 0,
                            "resultId": "864d9473-d9c3-4796-d2b4-03cffbacf879",
                            "content": "OK, 0 records retrieved in 4.049ms"
                        }
                    ]
                },
                "currentHeight": 300,
                "currentSet": 1,
                "statements": [
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 0,
                            "length": 70
                        },
                        "contentStart": 16,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 70,
                            "length": 56
                        },
                        "contentStart": 71,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 126,
                            "length": 50
                        },
                        "contentStart": 145,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 176,
                            "length": 26
                        },
                        "contentStart": 177,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 202,
                            "length": 92
                        },
                        "contentStart": 246,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 294,
                            "length": 42
                        },
                        "contentStart": 295,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 336,
                            "length": 130
                        },
                        "contentStart": 416,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 466,
                            "length": 118
                        },
                        "contentStart": 525,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 584,
                            "length": 37
                        },
                        "contentStart": 586,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 621,
                            "length": 55
                        },
                        "contentStart": 622,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 676,
                            "length": 62
                        },
                        "contentStart": 677,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 738,
                            "length": 86
                        },
                        "contentStart": 739,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 824,
                            "length": 123
                        },
                        "contentStart": 825,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 947,
                            "length": 58
                        },
                        "contentStart": 974,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 1005,
                            "length": 74
                        },
                        "contentStart": 1028,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 1079,
                            "length": 52
                        },
                        "contentStart": 1103,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 1131,
                            "length": 46
                        },
                        "contentStart": 1153,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 1177,
                            "length": 1
                        },
                        "contentStart": 1176,
                        "state": 3
                    }
                ]
            },
            "data": []
        },
        {
            "state": {
                "start": 1,
                "end": 43,
                "language": "mysql",
                "currentSet": 1,
                "statements": [
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 0,
                            "length": 345
                        },
                        "contentStart": 16,
                        "state": 3
                    }
                ]
            },
            "data": []
        }
    ]
}