from flask import Flask, request, render_template
from pokerodds import odds

def round_to_three_sig_figs(number):
    if number == 0:
        return 0
    else:
        from math import floor, log10
        magnitude = floor(log10(abs(number)))
        return round(number, 3 - magnitude - 1)

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def home():
    result = []
    error_message = ''
    hands = []  # Initialize hands to avoid UnboundLocalError
    cards = [
    "AS", "KS", "QS", "JS", "10S", "9S", "8S", "7S", "6S", "5S", "4S", "3S", "2S",
    "AH", "KH", "QH", "JH", "10H", "9H", "8H", "7H", "6H", "5H", "4H", "3H", "2H",
    "AD", "KD", "QD", "JD", "10D", "9D", "8D", "7D", "6D", "5D", "4D", "3D", "2D",
    "AC", "KC", "QC", "JC", "10C", "9C", "8C", "7C", "6C", "5C", "4C", "3C", "2C"
]

    if request.method == 'POST':
        #try:
            num_hands = int(request.form['num_hands'])
            hands = [[request.form[f'hand{i}_card1'], request.form[f'hand{i}_card2']] for i in range(1, num_hands + 1)]
            
            num_community_cards = int(request.form['num_community_cards'])
            community_cards = [request.form[f'community_card{i}'] for i in range(1, num_community_cards + 1)]
            result = odds(hands, community_cards)  # Pass processed input to the odds function
        #except Exception as e:
        #    error_message = "Invalid input format. Please check your input and try again."

    Ress = ""
    for n, hand in enumerate(hands):
        Ress += f"Hand {n + 1} ({hand[0]}, {hand[1]}): {round_to_three_sig_figs(result[n])}% "

    return render_template('index.html', result=Ress, error_message=error_message, cards=cards)

if __name__ == '__main__':
    app.run(debug=True)
