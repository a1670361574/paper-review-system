<script setup>
import { ref, reactive } from 'vue';
import InputDataForm from './InputDataForm.vue'

const haveTable = ref(false);
const tableData = ref([
    {
        studentID: '190110672',
        studentName: 'Zhang',
        tutorName: 'Wang',
        instituteName: 'HIT High Performance Compute Center',
        judges1: 'Xia',
        judges2: 'Zeng',
        checker: 'Wen',
        edit: false
    },
    {
        studentID: '200337859',
        studentName: 'Yang',
        tutorName: 'Liu',
        instituteName: 'HIT Biotech Center',
        judges1: 'Lu',
        judges2: 'Wang',
        checker: 'Li',
        edit: false
    },
    {
        studentID: '190110545',
        studentName: 'Albert',
        tutorName: 'Joanna',
        instituteName: 'HIT Data Processing Center',
        judges1: 'Zhang',
        judges2: 'Li',
        checker: 'Pang',
        edit: false
    },
    {
        studentID: '190110653',
        studentName: 'Huang',
        tutorName: 'Ai',
        instituteName: 'HIT Some Center',
        judges1: 'Wei',
        judges2: 'Zhang',
        checker: 'Liu',
        edit: false
    },
])

const colName = {
    studentID: 'Student ID',
    studentName: 'Student Name',
    tutorName: 'Tutor Name',
    instituteName: 'Institute Name',
    judges1: 'Judges 1',
    judges2: 'Judges 2',
    checker: 'Checker'
}

const exportTable = ref({})

function deleteRow(index) {
    tableData.value.splice(index, 1)
}

function addRow(data) {
    tableData.value.push(data)
}

</script>

<template>
    <el-switch v-model="haveTable" active-text="Have table data" inactive-text="No data" />
    <template v-if="haveTable">
        <el-table :data="tableData" stripe style="width: 100%" :row-style="{height: '50px'}">
            <el-table-column type="index" width="50" />
            <el-table-column :label="colName.studentID">
                <template #default="scope">
                    <el-input v-if="scope.row.edit" v-model="scope.row.studentID" :placeholder="colName.studentID" />
                    <span v-else>{{scope.row.studentID}}</span>
                </template>
            </el-table-column>

            <el-table-column :label="colName.studentName" width="140">
                <template #default="scope">
                    <el-input v-if="scope.row.edit" v-model="scope.row.studentName"
                        :placeholder="colName.studentName" />
                    <span v-else>{{scope.row.studentName}}</span>
                </template>
            </el-table-column>

            <el-table-column :label="colName.tutorName">
                <template #default="scope">
                    <el-input v-if="scope.row.edit" v-model="scope.row.tutorName" :placeholder="colName.tutorName" />
                    <span v-else>{{scope.row.tutorName}}</span>
                </template>
            </el-table-column>

            <el-table-column label="Institute Name" width="300">
                <template #default="scope">
                    <el-input v-if="scope.row.edit" v-model="scope.row.instituteName"
                        :placeholder="colName.instituteName" />
                    <span v-else>{{scope.row.instituteName}}</span>
                </template>
            </el-table-column>

            <el-table-column label="Judges 1">
                <template #default="scope">
                    <el-input v-if="scope.row.edit" v-model="scope.row.judges1" :placeholder="colName.judges1" />
                    <span v-else>{{scope.row.judges1}}</span>
                </template>
            </el-table-column>

            <el-table-column label="Judges 2">
                <template #default="scope">
                    <el-input v-if="scope.row.edit" v-model="scope.row.judges2" :placeholder="colName.judges2" />
                    <span v-else>{{scope.row.judges2}}</span>
                </template>
            </el-table-column>

            <el-table-column label="Checker">
                <template #default="scope">
                    <el-input v-if="scope.row.edit" v-model="scope.row.checker" :placeholder="colName.checker" />
                    <span v-else>{{scope.row.checker}}</span>
                </template>
            </el-table-column>

            <el-table-column fixed="right" label="Operations" width="180">
                <template #default="scope">

                    <template v-if="scope.row.edit">
                        <el-button type="success" plain size="small" @click.prevent="scope.row.edit=false">
                            Done
                        </el-button>
                    </template>
                    <template v-else>
                        <el-button type="primary" plain size="small" @click.prevent="scope.row.edit=true">
                            Edit
                        </el-button>
                        <el-button type="danger" plain size="small" @click.prevent="deleteRow(scope.$index)">
                            Remove
                        </el-button>
                    </template>
                </template>
            </el-table-column>
        </el-table>
        <el-divider />
        <el-button type="primary" @click="tableData.push({edit:true})">Add Data</el-button>
        <el-button type="success" @click="exportTable = Array.from(tableData)">Export Data</el-button>
        <el-divider />
        <p>Export Array = {{exportTable}}</p>
    </template>
    <el-empty v-else description="No data" />
</template>
