class Font:
     def SD(text):
          style = {
            'a':'ᴀ',
            'b':'ʙ',
            'c':'ᴄ',
            'd':'ᴅ',
            'e':'ᴇ',
            'f':'ғ',
            'g':'ɢ',
            'h':'ʜ',
            'i':'ɪ',
            'j':'ᴊ',
            'k':'ᴋ',
            'l':'ʟ',
            'm':'ᴍ',
            'n':'ɴ',
            'o':'ᴏ',
            'p':'ᴘ',
            'q':'ǫ',
            'r':'ʀ', 
            's':'s',
            't':'ᴛ',
            'u':'ᴜ',
            'v':'ᴠ',
            'w':'ᴡ',
            'x':'x',
            'y':'ʏ',
            'z':'ᴢ',
            '1':'𝟷',
            '2':'𝟸',
            '3':'𝟹',
            '4':'𝟺',
            '5':'𝟻',
            '6':'𝟼',
            '7':'𝟽',
            '8':'𝟾',
            '9':'𝟿',
            '0':'𝟶'          
          }
          stylized_text = ""
          for char in text:
              stylized_text += style.get(char, char)
          return stylized_text
