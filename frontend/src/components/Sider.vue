<script setup>
import { ref } from 'vue';

const sider_default_active = ref("1")
function clickFunc(str) {
    window.location.href = '#/' + str
}
</script>

<template>
    <el-menu :default-active="sider_default_active" class="menu-vertical">
        <el-sub-menu index="1">
            <template #title>
                OD Arrangement
            </template>
            <el-menu-item-group>
                <template #title><span>To be filled</span></template>
                <el-menu-item index="1-1" @click="clickFunc('')">Upload Page</el-menu-item>
                <el-menu-item index="1-2" @click="clickFunc('odpage')">Mulit-table Page</el-menu-item>
            </el-menu-item-group>
        </el-sub-menu>
        <el-menu-item index="2" @click="clickFunc('table')">Something</el-menu-item>
        <el-menu-item index="3" @click="clickFunc('emptyData')">Result Page</el-menu-item>
    </el-menu>
</template>



<style>
.menu-vertical {
    min-height: 400px;
}

</style>