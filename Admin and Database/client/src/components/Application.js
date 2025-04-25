import React, { useState } from "react";

const Application = ({ application }) => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="max-w-xl mx-auto bg-white rounded-2xl shadow-lg overflow-hidden border mb-6 hover:shadow-xl transition-shadow duration-300">
      {/* Header */}
      <div
        className="flex justify-between items-center px-6 py-4 cursor-pointer bg-gray-100 hover:bg-gray-200 transition-colors duration-300"
        onClick={() => setIsOpen(!isOpen)}
      >
        <div>
          <h2 className="text-xl font-semibold text-gray-800">
            Application #{application._id || "N/A"}
          </h2>
          <p className="text-sm text-gray-600">
            KYC Status:
            <span
              className={`ml-2 px-2 py-1 rounded-full text-white text-xs font-semibold ${
                application.kyc_status === "verified"
                  ? "bg-green-500"
                  : "bg-red-500"
              }`}
            >
              {application.kyc_status}
            </span>
          </p>
        </div>
        <button className="text-blue-600 font-medium underline">
          {isOpen ? "Collapse" : "Expand"}
        </button>
      </div>

      {/* Expanded Content */}
      {isOpen && (
        <div className="px-6 py-4 space-y-4 transition-all duration-300 bg-gray-50">
          {/* Aadhar Details */}
          <div className="bg-white p-4 rounded-lg shadow-inner">
            <h3 className="text-lg font-semibold mb-2">Aadhar Details</h3>
            <p><strong>Name:</strong> {application.adhar_details.name}</p>
            <p><strong>Card No:</strong> {application.adhar_details.identity_card_no}</p>
            <p><strong>DOB:</strong> {application.adhar_details.date_of_birth}</p>
            <p><strong>Sex:</strong> {application.adhar_details.sex}</p>
            <p><strong>Address:</strong> {application.adhar_details.address}</p>
            <p><strong>Country:</strong> {application.adhar_details.country}</p>
            <p><strong>True Documents:</strong> {application.adhar_details.True_Documents}</p>
          </div>

          {/* DL Details */}
          <div className="bg-white p-4 rounded-lg shadow-inner">
            <h3 className="text-lg font-semibold mb-2">DL Details</h3>
            <p><strong>Name:</strong> {application.dl_details.name}</p>
            <p><strong>Card No:</strong> {application.dl_details.identity_card_no}</p>
            <p><strong>DOB:</strong> {application.dl_details.date_of_birth}</p>
            <p><strong>Sex:</strong> {application.dl_details.sex}</p>
            <p><strong>Address:</strong> {application.dl_details.address}</p>
            <p><strong>Country:</strong> {application.dl_details.country}</p>
            <p><strong>True Documents:</strong> {application.dl_details.True_Documents}</p>
          </div>

          {/* Summary Info */}
          <div className="text-gray-700">
            <p><strong>Info Match Score:</strong> {application.info_match_score}/10</p>
            <p><strong>Customer Valid:</strong> {application.customer_valid ? "Yes" : "No"}</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default Application;
