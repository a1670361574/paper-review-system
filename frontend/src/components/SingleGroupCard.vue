<script setup>
import { ref } from 'vue';

const curDayArr = ref([
    { studentName: "Zhang", tutorName: "Liu", time: "8:30-9:30", comment: "something" },
    { studentName: "Li", tutorName: "Wang", time: "9:30-10:30", comment: "something" },
    { studentName: "Pang", tutorName: "Huang", time: "10:30-11:30", comment: "something" },
])
</script>

<template>
    <el-table :data="curDayArr" style="width: 100%">
        <el-table-column prop="studentName" label="Student Name" width="140px" />
        <el-table-column prop="tutorName" label="Tutor Name" />
        <el-table-column prop="time" label="Time" />
        <el-table-column prop="comment" label="Comment" />
    </el-table>
</template>

