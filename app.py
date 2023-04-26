import streamlit as st
import hafez


def main():

    # poem = hafez.get_poem(1)
    # poems = hafez.search('صبا')
    poems = hafez.omen()
    st.write(poems)


if __name__ == '__main__':
    main()
