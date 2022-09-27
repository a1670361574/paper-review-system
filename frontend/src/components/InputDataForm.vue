<template>
    <el-form :inline="true" :model="formInline" class="input_form" label-width="80px">
        <el-form-item>
            <el-input v-model="formInline.studentID" placeholder="Student ID" />
        </el-form-item>
        <el-form-item>
            <el-input v-model="formInline.studentName" placeholder="Student Name" />
        </el-form-item>
        <el-form-item>
            <el-input v-model="formInline.tutorName" placeholder="Tutor Name" />
        </el-form-item>
        <el-form-item>
            <el-input v-model="formInline.instituteName" placeholder="Institute Name" />
        </el-form-item>
        <el-form-item>
            <el-input v-model="formInline.judges1" placeholder="Judges 1" />
        </el-form-item>
        <el-form-item>
            <el-input v-model="formInline.judges2" placeholder="Judges 2" />
        </el-form-item>
        <el-form-item>
            <el-input v-model="formInline.checker" placeholder="Checker" />
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="$emit('addData',formInline)">Add</el-button>
        </el-form-item>
    </el-form>
</template>
  
<script lang="ts" setup>
import { emitChangeFn } from 'element-plus';
import { reactive } from 'vue'

defineEmits(['addData'])

const formInline = reactive({
    studentID: '',
    studentName: '',
    tutorName: '',
    instituteName: '',
    judges1: '',
    judges2: '',
    checker: ''
})

</script>

<style>
.el-form-item {
    margin-right: 10px !important;
}

.input_form {
    margin-top: 20px;
}
</style>
  