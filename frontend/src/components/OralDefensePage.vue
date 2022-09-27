<script setup>
import SingleGroupCard from './SingleGroupCard.vue';
</script>

<template>
    <el-row>
        <el-col v-for="(o, index) in 2" :key="o" :span="8" :offset="index > 0 ? 2 : 0">
            <el-card class="box-card">
                <template #header>
                    <div class="card-header">
                        <span>09-26 Group {{o}}</span>
                    </div>
                </template>
                <SingleGroupCard />
            </el-card>
        </el-col>
    </el-row>


</template>

<style>
.card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.item {
    margin-bottom: 18px;
}

.box-card {
    width: 500px;
}
</style>