<template>
    <div v-if="isLoading" class="loading-container">
	    <div class="loading">
		    <Fade-loader :color="loadingcol" />
	    </div>
    </div>
    <div class="grid gird-rows-6  grid-cols-3">
        <div class="row-span-1 col-span-3 text-4xl text-align-left pt-12 text-center">
            당신의 <span class="bg-red-500 text-white hover:bg-white hover:text-red-500">MARVEL TWIN HERO</span>를 찾아보세요!🦄
        </div>

        <textarea placeholder="당신의 성격을 자유롭게 적어주세요!" class="row-span-1 col-span-3 m-5 focus:ring-red-300 focus:border-red-500" v-model="inputValue" type="text"></textarea>
        
        <div class="row-span-1 col-span-3">
          <button class="text-red-700 m-5 p-2 hover:text-white border border-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2 dark:border-red-500 dark:text-red-500 dark:hover:text-white dark:hover:bg-red-600 dark:focus:ring-red-900" @click="callPythonFunction">Submit</button>
        </div>
        <div class="text-center p-4 text-2xl col-span-3">❗결과 출력까지 1~2분 가량 소요되니, 창을 닫지 말고 기다려주세요❗</div>
        <div class="row-span-4 col-span-3 m-8" v-show="stats == 1">
              <div class="bg-slate-100 text-center p-4 text-2xl">당신의 트윈 히어로는 <span class="bg-red-200">{{ result }}</span>입니다.🎉</div>
              <div class="bg-slate-100 text-center p-4"><span class="bg-red-200">{{ result }}</span>은 어떤 히어로일까요?</div>
              <div class="bg-white">{{ desc }}</div>
              <br>
              <div class="bg-white text-center p-8 text-3xl">당신의 twin hero에 대해 reddit 유저들은 어떤 이야기를 나눴을까요?</div>
              <div>다음은 reddit의 'Marvel' 서브레딧에서 당신의 twin hero에 대해 검색한 결과를 wordcloud로 나타낸 이미지입니다.</div>
              <div class="place-content-center p-5"><img src="@/assets/wordcloud.png" /></div>
              <div>다음은 당신과 친한 친구 히어로 입니다.</div>
              <div class="col-span-3">당식과 가장 친한 친구 히어로는 ... </div>
              <div class="text-center p-4"><span class="text-2xl">{{ bf }}</span></div>
        </div>
    </div>


</template>

<script>

import axios from 'axios'
import FadeLoader from 'vue-spinner/src/FadeLoader.vue'


  export default {
  data() {
    return {
      inputValue: '',
      result: '',
      desc:'',
      stats:0,
      isLoading: false,
      loadingcol: "#e23636"

    };
  },
  components: { FadeLoader },
  methods: {

    async callPythonFunction() {
      const urls = 'http://127.0.0.1:5000/heromatch/'+this.inputValue 
      console.log(urls) 
      this.isLoading = true;
      const response = await axios.get(urls);
      this.isLoading = false;  
      this.result = response.data.name;
      this.desc = response.data.desc;
      this.bf = response.data.bf; 
      this.stats = 1;
    }
  }
};
</script>
<style scoped>
@font-face {
    font-family: 'NeoDunggeunmoPro-Regular';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2302@1.0/NeoDunggeunmoPro-Regular.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}

div {
  font-family: 'NeoDunggeunmoPro-Regular';
}
span {
  font-family: 'NeoDunggeunmoPro-Regular';
}

.loading {
  z-index: 2;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  box-shadow: rgba(0, 0, 0, 0.1) 0 0 0 9999px;
}
</style>