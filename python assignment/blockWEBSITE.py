# code to block the facebook.com website
def block_fb_website(website):
    try:
        path_of_hosts_file = r'C:\Windows\System32\drivers\etc\hosts'
        redirect_ip = '127.0.0.1'

        with open(path_of_hosts_file, 'a') as file:  # opening host_path to append
            file.write(f'\n{redirect_ip} {website}')  # blocking the website

        print(f'{website} blocked.')
    except Exception as exp:
        print('Error:', str(exp))


if __name__ == "__main__":
    website_to_block = "facebook.com"
    block_fb_website(website_to_block)
