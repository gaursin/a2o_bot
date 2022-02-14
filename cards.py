CARD_CONTENT_TO_BDAY_PERSON = {
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "type": "AdaptiveCard",
    "version": "1.1",
    "body":
    [
    {
    "type": "ColumnSet",
    "columns":
        [
            {
            "type": "Column",
                "items": [
                        {
                            "type": "Image",
                            "style": "Person",
                            "url": "https://icons.iconarchive.com/icons/mohsenfakharian/christmas/512/cake-icon.png",
                            "size": "Medium",
                            "height": "75px"
                        }
                    ],
                "width": "auto"
            }
        ]
    },



        {
            "type": "TextBlock",
            "text": "",
            "size": "medium",
            "weight": "light",
            "color": "Accent"

        },
          {
            "type": "TextBlock",
            "text": "Happy Birthday! Wishing you a day filled with happiness and a year filled with joy.",
            "weight": "bolder",
            "wrap": True


        },


        {

            "type": "TextBlock",
            "text": "Check out the wishes from your teammates on the A2O Birthday Board",
            "spacing":"small",
            "weight":"Light",
            "wrap": True

        },

        {

            "type": "TextBlock",
            "text": "YOUR A2O FAMILY",
            "weight": "Lighter",
            "color": "Accent",
            "wrap": True

        }

    ],

        "actions": [
        {
            "type": "Action.OpenUrl",
            "title": "A2O Birthday Board",
            "id": "",
            "style": "positive",
            "url": "https://ciscocx.kudoboard.com/"
        }
]

}

CARD_CONTENT_TO_EVERYONE = {
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "type": "AdaptiveCard",
    "version": "1.1",
    "body":
    [
    {
    "type": "ColumnSet",
    "columns":
           [
                {
                   "type": "Column",
                    "items": [
                        {
                            "type": "Image",
                            "style": "Person",
                            "url": "https://icons.iconarchive.com/icons/mohsenfakharian/christmas/512/cake-icon.png",
                            #"url":"https://www.sampleposts.com/wp-content/uploads/2020/04/Farewell-Quotes-For-Final-Year-Students.png",
                            "size": "Medium",
                            "height": "75px"
                        }
                ],
                    "width": "auto"
                }
            ]
        },
                {
                    "type": "TextBlock",
                    "text": "",
                    "size": "medium",
                    "weight": "light",
                    "color": "Accent"

                 },

                {

                    "type": "TextBlock",
                    "text": "",
                    "wrap": True,
                    "weight":"bolder",
                    "spacing":"small"


                },
                {

                    "type": "TextBlock",
                    "text": "Send your wishes on the A2O Birthday Board!",
                    "wrap": True,
                    "weight": "Light",
                    "spacing":"small"


                },
                {

                "type": "TextBlock",
                "text": "YOUR A2O FAMILY",
                "weight": "Lighter",
                "color": "Accent",
                "wrap": True

                }
    ],

            "actions": [
                {
                    "type": "Action.OpenUrl",
                    "title": "A2O Birthday Board",
                    "id": "",
                    "style": "positive",
                    "url": "https://ciscocx.kudoboard.com/"
                }
                ]
}

REMINDER_CARD = {
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "type": "AdaptiveCard",
    "version": "1.1",
    "body": [
        {
      "type": "ColumnSet",
      "columns": [
                {
        "type": "Column",
                    "items": [
                        {

                            "type": "Image",
                            "style": "Person",
                            "url": "https://icons.iconarchive.com/icons/blackvariant/button-ui-microsoft-office-apps/1024/Microsoft-Reminders-icon.png",
                            "size": "Medium",
                            "height": "40px"
                        }
                    ],
                    "width": "auto"
                }
            ]
        },
                {
                    "type": "TextBlock",
                    "text": "Reminder!",
                    "size": "medium",
                    "weight": "light",
                    "color": "Accent"

       },

        {

            "type": "TextBlock",
            "text": "",
            "wrap": True,
            "weight":"bolder",
            "spacing":"small"


        }]


}
SUCCESS_CARD = {
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "type": "AdaptiveCard",
    "version": "1.1",
    "body": [
        {
      "type": "ColumnSet",
      "columns": [
        {
        "type": "Column",
                    "items": [
                        {
                            "type": "Image",
                            "style": "Person",
                            "url": "https://icons.iconarchive.com/icons/graphicloads/100-flat-2/256/check-1-icon.png",
                            "size": "Medium",
                            "height": "40px"
                        }
                    ],
                    "width": "auto"
                }
            ]
        },
            {
                "type": "TextBlock",
                "text": "",
                "weight": "light",
                "color": "Accent"

       }
    ]


}
