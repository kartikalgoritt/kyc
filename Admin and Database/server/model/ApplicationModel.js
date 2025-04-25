import mongoose from "mongoose";

const ApplicationSchema = new mongoose.Schema({
    adhar_details: {
        type: Object,
        required: true,
        schema: {
            name: { type: String, required: true },
            identity_card_no: { type: String, required: true },
            date_of_birth: { type: String, match: /^\d{4}-\d{2}-\d{2}$/, required: true },
            sex: { type: String, enum: ['M', 'F'], required: true },
            address: { type: String, required: true },
            country: { type: String, required: true }
        }
    },
    dl_details: {
        type: Object,
        required: true,
        schema: {
            name: { type: String, required: true },
            identity_card_no: { type: String, required: true },
            date_of_birth: { type: String, match: /^\d{4}-\d{2}-\d{2}$/, required: true },
            sex: { type: String, enum: ['M', 'F'], required: true },
            address: { type: String, required: true },
            country: { type: String, required: true }
        }
    },
    info_match_score: { type: Number, min: 1, max: 10, required: true },
    customer_valid: { type: Boolean, required: true },
    kyc_status: {
        type: String,
        enum: ['verified', 'not_verified'],
        required: true,
        default: 'not_verified'
    }
}, {collection:'documents'});

const Application = mongoose.model('Applications', ApplicationSchema);

export default Application;