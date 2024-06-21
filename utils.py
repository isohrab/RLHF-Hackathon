import re
from IPython.display import display, HTML

def extract_answer(text):
    # Define the regex pattern
    text = text.replace("<|assistant|>", "<gpt>")
    text = text.replace("<|end|>", "</s>")
    pattern = re.compile(r'<gpt>(.*?)</s>', re.DOTALL)
    matches = pattern.findall(text)
    if matches:
        return  matches[0]
    else:
        print("No match found")



def show_responses(t1,t2):   
    # HTML template to display texts side by side
    html_template = f"""
    <div style="display: flex; flex-direction: row; width: 100%;">
      <div style="width: 50%;flex: 1; padding: 10px; border: 1px solid black; margin-right: 10px;">
        <h3>Response 1</h3>
          <p>
          {t1}
          </p>
      </div>
      <div style="width: 50%;flex: 1; padding: 10px; border: 1px solid black;">
        <h3>Response 2</h3>
          <p>
          {t2}
          </p>
      </div>
    </div>
    """
    
    # Display the HTML
    display(HTML(html_template))