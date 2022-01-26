"""
# My Second app
DESC: app for Recipy recommendation

"""
from lib2to3.pgen2.pgen import DFAState
import shutil
import streamlit as st
import pandas as pd
import gzip

with gzip.open('recipy/recipeitems-latest.json.gz', 'rb') as f_in:
    with open('recipy/recipeitems-latest.json', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


@st.cache(allow_output_mutation=True)
def get_df():
    df = pd.read_json('recipy/recipeitems-latest.json', lines=True)
    df['description'] = df.description.str.lower()
    return df

st.title('recipy recommendation')

recipes = get_df()

st.write('recipes quantity: ', len(recipes))

st.write(recipes.head())

with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("salt 鹽巴")
        st.image("https://media.istockphoto.com/photos/salt-in-wooden-table-picture-id827818618?k=20&m=827818618&s=612x612&w=0&h=46oA2A7pwTIB1zkUkBZuyabRfVqfohNgmpN7UVT9xmg=")

    with col2:
        st.subheader("pepper 胡椒")
        st.image("https://media.istockphoto.com/photos/ground-black-pepper-in-a-wooden-bowl-and-peppercorns-on-a-white-top-picture-id1301622377?b=1&k=20&m=1301622377&s=170667a&w=0&h=mCcdI9-VhSmsoiA6-2WVHFJYDk0SXWAFNctLGHhT7lY=")

    with col3:
        st.subheader("oregano 奧勒岡")
        st.image("https://media.istockphoto.com/photos/dried-oregano-on-table-picture-id624125706?b=1&k=20&m=624125706&s=170667a&w=0&h=dRlUZRYBq46Sypu9VUianX7GyPv05soFvb03hnQ-wvI=")
    
    col4, col5, col6 = st.columns(3)

    with col4:
        st.subheader("sage 鼠尾草")
        st.image("https://media.istockphoto.com/photos/fresh-green-sage-leaves-isolated-on-white-background-picture-id1273827154?b=1&k=20&m=1273827154&s=170667a&w=0&h=t0KXK2Em8maubZrxuU2YK19H42HODYUMZFqfs-jJlVw=")

    with col5:
        st.subheader("parsley 巴西里")
        st.image("https://media.istockphoto.com/photos/bunch-of-fresh-parsley-leafs-isolated-on-white-picture-id1089491274?b=1&k=20&m=1089491274&s=170667a&w=0&h=fi5J0-sWsCh_SEo6ZJwajAAH7k1DdYsaXIUfgb463r0=")

    with col6:
        st.subheader("rosemary 迷迭香")
        st.image("https://media.istockphoto.com/photos/fresh-rosemary-herb-on-white-background-picture-id185405924?b=1&k=20&m=185405924&s=170667a&w=0&h=A7PPcqURR35ifKqhLmtqZpuoU9gffOcZ6afXiD4Jvuk=")
    
    col7, col8, col9 = st.columns(3)

    with col7:
        st.subheader("tarragon 龍蒿")
        st.image("https://media.istockphoto.com/photos/tarragon-picture-id504070278?b=1&k=20&m=504070278&s=170667a&w=0&h=_xPO38J2gaGxbo4zQsD5Rb7k5BVauUIXh5EN4tbEm_I=")

    with col8:
        st.subheader("thyme 百里香")
        st.image("https://media.istockphoto.com/photos/fresh-garden-thyme-herb-on-a-rustic-table-picture-id1298350451?b=1&k=20&m=1298350451&s=170667a&w=0&h=2aGMkN2oWzRiQ_f25R3MEwBTUTQiLihpSgRGeb-kfmw=")

    with col9:
        st.subheader("paprika 紅椒粉")
        st.image("https://media.istockphoto.com/photos/paprika-picture-id471346203?b=1&k=20&m=471346203&s=170667a&w=0&h=0Jqrx2GIXqbpHc1yTfxbQPDlv5aVJ-Bpzc6Yobz9p9M=")



spice_list = ['salt', 'pepper', 'oregano', 'sage', 'parsley', 'rosemary', 'tarragon', 'thyme', 'paprika', 'cumin']
options = st.multiselect("enter which spice you are interested(multi-select)", spice_list, spice_list[0])


spice_df = pd.DataFrame(dict((spice, recipes.ingredients.str.contains(spice)) for spice in spice_list))

selection = spice_df.query(' & '.join(options))
st.write(len(selection))

selected_result = recipes.iloc[selection.index]
selected_result = selected_result.dropna(subset=['image', 'url']).head(4).reset_index()
st.write(selected_result)

with st.container():
    res1, res2 = st.columns(2)

    with res1:
        st.subheader(selected_result.name[0])
        st.image(selected_result.image[0])
        st.write(f'check out recipy [here]({selected_result.url[0]})')

    with res2:
        st.subheader(selected_result.name[1])
        st.image(selected_result.image[1])
        st.write(f'check out recipy [here]({selected_result.url[1]})')

    res3, res4 = st.columns(2)

    with res3:
        st.subheader(selected_result.name[2])
        st.image(selected_result.image[2])
        st.write(f'check out recipy [here]({selected_result.url[2]})')
    
    with res4:
        st.subheader(selected_result.name[3])
        st.image(selected_result.image[3])
        st.write(f'check out recipy [here]({selected_result.url[3]})')

