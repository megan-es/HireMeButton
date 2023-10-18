# Bokeh model and layout imports
from bokeh.layouts import column
from bokeh.models import Button, Div

# Bokeh IO imports
from bokeh.io import show, curdoc

# Create the Hire Me! button
button = Button(label="Hire Me!", button_type="success")

# Create hidden Div to show info when button is clicked
div = Div(text="", width=600, height=600)

# HTML content to be displayed when button is clicked
content = """
<br>
    <b style='font-size: 1.2em;'>About Me:</b>
    <ul style='padding-left: 20px; margin-top: 10px;'>
        <li>Data Analyst proficient in SQL, Python, Excel, and Tableau</li>
        <li>Currently based out of the Greater Seattle Area</li>
        <li>Extremely self-motivated, skilled in collaboration and on-the-fly problem solving</li>
        <li>4+ years experience in data-driven investigations of criminal activity</li>
        <li>3+ years experience working with education data in K-12 and higher ed</li>
        <li>University of Oregon and University of Puget Sound Alum</li>
    </ul>
    <ul style='list-style: none; padding-left: 0px;'>
        <li><a href='https://www.linkedin.com/in/-megan-e-smith/'>LinkedIn</a></li>
        <li><a href='https://github.com/megan-es'>Github</a></li><li>
        <a href='https://public.tableau.com/app/profile/megan.es/vizzes'>Tableau Public</a></li>
    </ul>
"""
def update():
    div.text = content
    
button.on_click(update)

# Organize layout and show
layout = column(button, div)
curdoc().add_root(layout) 
show(layout)
