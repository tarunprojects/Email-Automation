#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
import discord
import os
import time
import discordpart
TOKEN = ''
GUILD = ''
client = discord.Client()

driver = webdriver.Chrome(executable_path=r"C:\Users\Desktop\chromedriver.exe")

def login ():
    try:
        driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=' +                'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1' +                '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
        driver.implicitly_wait(10)
        loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
        loginBox.send_keys("")

        nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
        nextButton[0].click()

        passWordBox = driver.find_element_by_xpath('//*[@id ="password"]/div[1]/div / div[1]/input')
        passWordBox.send_keys("")
        nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
        nextButton[0].click()

    except:
        print("Error with script")

def checkemail():
    unread_mails = driver.find_elements_by_xpath("//*[@class='zF']")
    for index, mails in enumerate(unread_mails):
        print(unread_mails[index])
        if unread_mails[index].is_displayed():
            try:
                unread_mails[index].click()
                driver.save_screenshot('text.png')
                driver.close()
            except:
                print("Error")

def sendingtoserver():
    print("Preparing to send image to server ")

    @client.event
    async def on_ready():
        print("Bot is getting ready to connect...")
        for guild in client.guilds:
            if guild.name == GUILD:
                break

        print(f'{client.user} is connected to the following guild:\n' 
              f'{guild.name}(id: {guild.id})\n')

        channel = client.get_channel(797128681284698133)
        await channel.send(file=discord.File('text.png'))
        os.remove('text.png')


login()
checkemail()
sendingtoserver()
client.run(TOKEN)

