<template>
    <el-menu :default-active="activeIndex" mode="horizontal" :ellipsis="false">
        <p class="header">Review Helper</p>
        <div class="flex-grow" />
        <el-switch class="switch" v-model="isDark" inline-prompt :active-icon="Moon" :inactive-icon="Sunny" />
        <el-menu-item index="1">
            Something
        </el-menu-item>
    </el-menu>
</template>

<script setup>
import { ref } from 'vue'
import { useDark } from '@vueuse/core';
import { Sunny, Moon } from '@element-plus/icons-vue'

const activeIndex = ref('1')
const isDark = useDark()
</script>

<style>
.switch {
    margin: auto;
    padding-right: 10px;
}

.flex-grow {
  flex-grow: 1;
}

.header {
  font-size: x-large;
  font-weight: bold;
  font-family: "Jetbrains Mono";
  margin: auto;
  align-items: center;
  justify-content: center;
}

.icon {
  margin-left: 4px;
}
</style>