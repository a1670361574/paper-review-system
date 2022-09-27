<template>
    <el-row>
        <el-col :span="24">
            <el-upload class="upload-demo" drag action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                multiple>
                <el-icon class="el-icon--upload">
                    <upload-filled />
                </el-icon>
                <div class="el-upload__text">
                    Drop file here or <em>click to upload</em>
                </div>
                <template #tip>
                    <div class="el-upload__tip">
                        Excel file with given format
                    </div>
                </template>
            </el-upload>
        </el-col>
    </el-row>
    <el-row justify="center">
        <el-button type="primary" plain :icon="Upload">
            Confirm Upload
        </el-button>
        <el-button type="danger" plain :icon="DocumentDelete">
            Delete
        </el-button>
    </el-row>
</template>

<script setup>
import { UploadFilled, Upload, DocumentDelete } from '@element-plus/icons-vue'
</script>

<style>
.el-upload__text {
    font-family: "Jetbrains Mono";
}
</style>