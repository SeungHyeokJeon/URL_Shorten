<template>
  <v-container>
    <v-row class="text-center" justify="center">

      <v-col class="mt-16" cols="12">
        <v-img
          :src="require('../assets/url.png')"
          class="my-2"
          contain
          height="200"
        />
      </v-col>

      <v-col class="mb-4" cols="12">
        <h1 class="display-2 font-weight-bold mb-3">
          URL Shorten Service
        </h1>
      </v-col>

      <v-col class="mb-4" cols="12">
        <v-text-field
          :rules="rules"
          v-model="origin_url"
          @keydown.enter="submit"
          autofocus
        ></v-text-field>
      </v-col>

      <v-col v-model="shorten_url" class="mb-4 gray" cols="8">
        <h2>{{shorten_url}}</h2>
      </v-col>

    </v-row>
  </v-container>
</template>

<script>
  import axios from "axios"
  import Vue from 'vue'
  import VueClipboard from 'vue-clipboard2'

  Vue.use(VueClipboard) //vue-clipboard2 사용설정

  export default {
    name: 'UrlShorten',

    data: () => ({
      rules: [
        // value => {
        //   const pattern = /(http|https):\/\/((\w+)[.])+(asia|biz|cc|cn|com|de|eu|in|info|jobs|jp|kr|mobi|mx|name|net|nz|org|travel|tv|tw|uk|us)(\/(\w*))*$/i;
        //   return pattern.test(value) || '유효하지 않은 URL 입니다'
        // },
      ],
      origin_url : '',
      shorten_url : '',
    }),

    methods: {
    submit () {
      axios.get('http://34.68.2.47:12098/url?url='+this.origin_url, { 
        result: this.shorten_url
      })
      .then((response) => {
        this.shorten_url= response.data.url
        this.$copyText(this.shorten_url)
      })
      .catch(() => {
        this.shorten_url= 'Incorrect URL'
      })
    }
    }
  }
</script>