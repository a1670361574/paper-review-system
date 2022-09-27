<script lang="ts" setup>
import Header from './components/Header.vue'
import Sider from './components/Sider.vue'
import UploadPage from './components/UploadPage.vue'
import TablePage from './components/TablePage.vue'
import ResultPage from './components/ResultPage.vue'
import { computed, ref } from 'vue';
import OralDefensePage from './components/OralDefensePage.vue'

const curPath = ref(window.location.hash)

window.addEventListener('hashchange', () => {
  curPath.value = window.location.hash
})

const routes = {
  '/': UploadPage,
  '/table': TablePage,
  '/emptyData': ResultPage,
  '/odpage':OralDefensePage
}

const currentView = computed(() => {
  return routes[curPath.value.slice(1) || '/']
})
</script>
  
<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <Header />
      </el-header>
      <el-container>
        <el-aside width="200px">
          <Sider />
        </el-aside>
        <el-main>
          <component :is="currentView" />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>