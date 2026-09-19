# Mr.Bentover - Discord Bot to cook U

Mr Bentover is a discord Bot which it will analyze the last 4 messages and it will sugest a keyword and in that matching keyword it gives us a Gif in the chat . we can call him by calling "$Bentover"

## Prerequisites
- Python 3.10 or higher
- Discord developer account and Bot token 
- Hack club AI API Key
- GIPHY API Key

## Project Structure
```text
MrBentover/
├── .env               
├── .gitignore          
├── requirements.txt      
├── README.md           
├── Bot.py                 
│   ├──> GIF_prediction.py 
│   └──> shared.py         
│        └──> Gif_search.py 
│
└── main.py          
    ├──> GIF_prediction.py
    └──> shared.py
         └──> Gif_search.py

```

## Setup and Installation

1 . **clone the repo**
```bash
   git clone https://github.com/stairmoss/Mr.BentOver.git
   cd MrBentover
```

2. **Install the requirements**
```bash
   pip install pip download -r requirements.txt
   ```
3.**run the code**
```bash
  python3 Bot.py
  ```

4 **FEEL FREE TO CONTRIBUTE :3**