from threading import Thread
import requests
import time

def keep_awake():
    while True:
        try:
            requests.get("https://exclusivoonly-bot.onrender.com")
            print("✅ Mantendo bot acordado")
        except Exception as e:
            print(f"⚠️ Erro no keep-alive: {e}")
        time.sleep(240)  # 4 minutos

Thread(target=keep_awake, daemon=True).start()
import telebot
from flask import Flask, request

BOT_TOKEN = "8454551876:AAHUYLOtmxRHdzw71lmhuFIH5XtRZflyIZU"
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

# LINK DO SEU MERCADO PAGO
LINK_MERCADO_PAGO = "https://www.mercadopago.com.br/subscriptions/checkout?preapproval_plan_id=f4d54a4e08a44cdca47f7422c7fd0c50"

@app.route('/')
def home():
    return "🤖 @ExclusivoOnly_bot ONLINE! 🚀"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = f"""
🎁 *BEM-VINDO AO CONTEÚDO EXCLUSIVO!* 🔥

💎 *ACESSO VIP COMPLETO*
• Conteúdo adulto premium
• Mais de 100 mídias exclusivas
• Atualizações diárias
• Acesso vitalício

💳 *VALOR PROMOCIONAL*: R$ 5,00
📋 *Formas de pagamento*:
✅ PIX - Aprovação instantânea
✅ Cartão de Crédito
✅ Débito Bancário  
✅ Boleto Bancário

⚡ *GARANTIA*:
✅ Acesso imediato após pagamento
✅ Suporte 24h pelo @JoaoGM
✅ Conteúdo de alta qualidade

📲 *COMO COMPRAR*:
1️⃣ Clique no link abaixo
2️⃣ Escolha a forma de pagamento
3️⃣ Efetue o pagamento de R$ 5,00
4️⃣ Envie o comprovante para @JoaoGM

🔗 [CLIQUE AQUI PARA COMPRAR]({LINK_MERCADO_PAGO})

💬 *DÚVIDAS?* Chame @JoaoGM
    """
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown')

@bot.message_handler(commands=['comprar'])
def comprar_command(message):
    comprar_text = f"""
💎 *QUERO ACESSO IMEDIATO!* 🚀

💵 *Valor: R$ 5,00*
📋 *Pagamento por*:
• PIX (instantâneo)
• Cartão de Crédito
• Débito Bancário
• Boleto

🔗 [CLIQUE AQUI PARA COMPRAR]({LINK_MERCADO_PAGO})

📞 *Após o pagamento*:
• Envie o comprovante para @JoaoGM
• Acesso liberado em até 2 minutos

⚡ *Promoção por tempo limitado!*
    """
    bot.send_message(message.chat.id, comprar_text, parse_mode='Markdown')

@bot.message_handler(commands=['exclusivo'])
def exclusivo_command(message):
    preview_text = f"""
🔞 *PRÉVIA DO CONTEÚDO EXCLUSIVO* 🎬

🌸 *O que você vai encontrar*:
• Vídeos completos em HD
• Fotos sensuais exclusivas
• Conteúdo amateur real
• Cenas quentes e ousadas

📸 *Foto exclusiva de prévia*:
[Imagine aqui uma foto sensual]

💵 *Valor promocional*: R$ 5,00
💎 *Acesso vitalício*

📲 Use /comprar para acesso imediato!
🔗 [CLIQUE AQUI PARA COMPRAR]({LINK_MERCADO_PAGO})
    """
    bot.send_message(message.chat.id, preview_text, parse_mode='Markdown')

@bot.message_handler(commands=['info'])
def info_command(message):
    info_text = f"""
📞 *INFORMAÇÕES*:

💳 *Valor*: R$ 5,00
📋 *Formas de pagamento*:
• PIX (aprovacao instantânea)
• Cartão de Crédito
• Débito Bancário
• Boleto Bancário

⏰ *Liberação*: Imediata após comprovante
👤 *Atendimento*: @JoaoGM

🔗 [CLIQUE AQUI PARA COMPRAR]({LINK_MERCADO_PAGO})

💬 Envie /comprar para ir direto ao link!
    """
    bot.send_message(message.chat.id, info_text, parse_mode='Markdown')

@bot.message_handler(commands=['previa'])
def previa_command(message):
    previa_text = "🔞 *PRÉVIA EXCLUSIVA* - Aqui vai uma amostra do conteúdo quente que você vai ter acesso! 🎯"
    bot.send_message(message.chat.id, previa_text, parse_mode='Markdown')
    # bot.send_photo(message.chat.id, "URL_DA_SUA_FOTO_AQUI", caption="📸 Foto exclusiva do conteúdo VIP")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text.lower() in ['oi', 'ola', 'hello', 'hi']:
        bot.reply_to(message, "Olá! 😊 Use /start para ver nossos conteúdos exclusivos!")
    elif 'preco' in message.text.lower() or 'preço' in message.text.lower():
        bot.reply_to(message, "💵 Valor: R$ 5,00\nUse /comprar para adquirir!")
    else:
        bot.reply_to(message, "💬 Para nosso conteúdo exclusivo, use /start\nDúvidas? Chame @JoaoGM")

if __name__ == "__main__":
    print("BOT COMERCIAL INICIADO!")
    bot.remove_webhook()

    # Inicia o bot do Telegram em uma thread separada
    from threading import Thread

    Thread(target=bot.infinity_polling).start()

    # ✅ CORRETO: Usa a porta do Render
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)