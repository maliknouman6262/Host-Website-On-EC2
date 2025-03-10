from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', header=True)

@app.route('/services')
def services():
    return render_template('services.html', header=True)

@app.route('/contact')
def contact():
    return render_template('contact.html', header=True)

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html', header=True)

@app.route('/faq')
def faq():
    return render_template('faq.html', header=True)

@app.route('/pricing')
def pricing():
    return render_template('pricing.html', header=True)

@app.route('/about')
def about():
    return render_template('about.html', header=True)

@app.route('/redirect-to-services')
def redirect_to_services():
    return redirect(url_for('services'))

@app.route('/redirect-to-contact')
def redirect_to_contact():
    return redirect(url_for('contact'))

@app.route('/redirect-to-blog')
def redirect_to_blog():
    return redirect(url_for('blog'))
@app.route('/products')
def products():
    # Dummy data for products
    products = [
        {"name": "Agentic Ai", "category": "category1", "description": "It an advanced type of ai", "image": "product1.jpg"},
        {"name": "Ai Chatbot", "category": "category2", "description": "It design to solve users quires", "image": "product2.jpg"},
        # Add more products as needed
    ]
    return render_template('products.html', products=products) # Render the products page
@app.route('/ai_services')
def ai_services():
    return render_template('ai_services.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')
@app.route('/ai-agents')
def ai_agents():
    print("AI Agents page accessed")
    return render_template('ai-agents.html')
@app.route('/now-assist')
def now_assist():
    return render_template('now_assist.html')
if __name__ == '__main__':
    app.run(debug=True)
