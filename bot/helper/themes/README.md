## ***Custom Themes*** 🛠

- 🤖 **Tutorial** for how to make your Custom Themes.
- _Let's First Start with Utilities._

### ***Requirements :***
1. A Local Editor or Use [github.dev](https://github.dev)
2. **Sample File :** Check [zxzone_minimal.py](https://github.com/obscure-n8/ZxZone-Master-MLTB/blob/main/bot/helper/themes/zxzone_minimal.py)

---

#### ***Step 1:*** Open the Blank Editor and Paste the Codes of zxzone_minimal.py and name it `zxzone_custom.py`
You can give the `custom` as your choice, like `zxzone_futuristic.py`, etc

#### ***Step 2:*** Start by Editing and Making your Ultimate Design ✨️ and Save in this Folder
- _Things to Remember while Editing :_
  - Don't Change the Name Inside `{` `}` **(2nd Brackets)**
  - Don't Change the Variable Name like `ST_BN1_NAME`, etc
  - Don't Change the Class name ZxZoneStyle
  - Don't Use f-string like `f"{var}"`
***Sample Editing :***
```python
class ZxZoneStyle: # Don't Change This
    ST_BN1_NAME = '{sb1n}'
    # You can Change as Below !! -->
    ST_BN1_NAME = "It's {sb1n} ❤️" # Use Double Quotes, when using Single Quotes Inside
